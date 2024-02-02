import re
import os
import subprocess
import argparse


def strip_ansi_sequences(text):
    """Remove ANSI escape sequences from a string."""
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return strip_ansi_sequences(result.stdout)


def capture_cli_usage(project_root, repo_name, author, use_nix=False):
    """Dynamically determine and run the `--help` command for the project."""
    if use_nix:
        # Directly specifying the command for nix projects
        command = f"nix run github:{author}/{repo_name} -- --help"
        try:
            return run_command(command)
        except subprocess.CalledProcessError as e:
            return f"Error running command: {e}"

    # Assuming `project_root` has an executable CLI application
    command = f"{os.path.join(project_root, f'result/bin/{repo_name}')} --help"
    try:
        return run_command(command)
    except subprocess.CalledProcessError as e:
        return f"Error running command: {e}"


def git_tracked_directories(base_path):
    """Get a list of directories tracked by Git, excluding hidden directories."""
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "HEAD"],
            cwd=base_path,
            text=True,
            capture_output=True,
        )
        output = result.stdout
        directories = {
            os.path.dirname(file)
            for file in output.strip().split("\n")
            if "/" in file
            and not any(
                part.startswith(".") for part in os.path.dirname(file).split("/")
            )
        }
        return sorted(directories)
    except subprocess.CalledProcessError:
        return []


def directory_tree(path, make_links=False):
    """Generate a directory tree structure for directories tracked by Git."""
    tree = []
    tracked_dirs = git_tracked_directories(path)
    for dir in tracked_dirs:
        level = dir.count("/")
        indent = " " * 4 * level
        dir_name = os.path.basename(dir)
        dir_path = os.path.relpath(dir, path) if make_links else ""
        tree.append(
            f"{indent}[{dir_name}]({dir_path}/)"
            if make_links
            else f"{indent}{dir_name}/"
        )
    return "\n".join(tree)


def get_repo_name():
    return os.path.basename(os.path.normpath(os.getcwd()))


def generate_readme(
    path,
    include_dir_tree,
    include_links,
    include_nix,
    markdown_prefix_file,
    markdown_footer_file,
    author=None,
    repo_name=None,
    include_cli_usage=False,
    use_nix_for_cli=False,
):
    existing_content = ""
    if markdown_prefix_file and os.path.exists(markdown_prefix_file):
        with open(markdown_prefix_file, "r") as f:
            existing_content = f.read()

    readme_content = existing_content

    if not repo_name and not existing_content:
        repo_name = get_repo_name()
    readme_content += f"# {repo_name}\n"

    if include_dir_tree:
        dir_tree = directory_tree(path, make_links=include_links)
        readme_content += (
            "\n### Directory Tree\n\n"
            + ("\n```bash\n" + dir_tree + "\n```" if not include_links else dir_tree)
            + "\n"
        )

    if include_cli_usage:
        cli_usage_output = capture_cli_usage(
            path, repo_name, author, use_nix=use_nix_for_cli
        )
        readme_content += "\n### CLI Usage\n\n```bash\n" + cli_usage_output + "\n```\n"

    if include_nix:
        flake_show_output = run_command("nix flake show . --all-systems")
        readme_content += (
            "\n### Nix Flake Show\n\n```nix\n" + flake_show_output + "\n```\n"
        )

    if author:
        readme_content += f"\n---\n\n👤 **{author}**\n"

    if markdown_footer_file and os.path.exists(markdown_footer_file):
        with open(markdown_footer_file, "r") as f:
            readme_content += "\n" + f.read()

    return readme_content


def main():
    parser = argparse.ArgumentParser(description="Generate README.md content.")
    parser.add_argument(
        "--dir", help="Include directory tree structure", action="store_true"
    )
    parser.add_argument("--header", help="Path to the header markdown file", type=str)
    parser.add_argument("--footer", help="Path to the footer markdown file", type=str)
    parser.add_argument(
        "--flake-show", help="Include nix flake show output", action="store_true"
    )
    parser.add_argument("--author", help="GitHub username", type=str)
    parser.add_argument("--title", help="GitHub repository name", type=str)
    parser.add_argument(
        "--links", help="Turn directory tree into Markdown links", action="store_true"
    )
    parser.add_argument(
        "--usage", help="Include CLI application usage", action="store_true"
    )
    parser.add_argument(
        "--use-nix-run",
        help="Use nix to run the CLI help command",
        action="store_true",
    )
    args = parser.parse_args()

    repo_name = args.title if args.title else get_repo_name()
    readme_exists = os.path.exists("README.md")
    readme_content = generate_readme(
        ".",
        args.dir,
        args.links,
        args.flake_show,
        args.header,
        args.footer,
        args.author,
        repo_name,
        include_cli_usage=args.usage,
        use_nix_for_cli=args.use_nix_run,
    )

    with open("README.md", "w") as f:
        f.write(readme_content)

    if readme_exists:
        print("README.md existed and was overwritten.")
    else:
        print("README.md did not exist and was created.")
