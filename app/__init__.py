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
    include_flake_show,
    include_flake_info,
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

    if repo_name is not None and not readme_content:
        readme_content += f"# {repo_name}\n"

    repo_name = repo_name if repo_name else get_repo_name()

    if include_dir_tree:
        dir_tree = directory_tree(path, make_links=include_links)
        readme_content += (
            "\n### Directory\n\n"
            + ("\n```bash\n" + dir_tree + "\n```" if not include_links else dir_tree)
            + "\n"
        )

    if include_cli_usage:
        cli_usage_output = capture_cli_usage(
            path, repo_name, author, use_nix=use_nix_for_cli
        )
        readme_content += "\n### Usage\n\n```bash\n" + cli_usage_output + "\n```\n"

    if include_flake_info:
        flake_show_output = run_command("nix flake info .")
        readme_content += "\n### Flake Info\n\n```nix\n" + flake_show_output + "\n```\n"

    if include_flake_show:
        flake_show_output = run_command("nix flake show . --all-systems")
        readme_content += (
            "\n### Flake Outputs\n\n```nix\n" + flake_show_output + "\n```\n"
        )

    if author:
        readme_content += f"\n---\n\n👤 [**{author}**](https://github.com/{author})\n"

    if markdown_footer_file and os.path.exists(markdown_footer_file):
        with open(markdown_footer_file, "r") as f:
            readme_content += "\n" + f.read()

    return readme_content


def main():
    parser = argparse.ArgumentParser(description="Generate README.md content.")
    parser.add_argument("-a", "--author", help="GitHub username", type=str)
    parser.add_argument("-r", "--repo", help="GitHub repository name", type=str)
    parser.add_argument(
        "-o",
        "--output",
        help="Output file to write to, defaults to README.md",
        type=str,
        default="README.md",
    )
    parser.add_argument(
        "-d", "--dir", help="Include directory tree structure", action="store_true"
    )
    parser.add_argument(
        "-l",
        "--links",
        help="Turn directory tree into Markdown links",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--usage",
        help="Include CLI application usage by building with nix",
        action="store_true",
    )
    parser.add_argument(
        "-fs", "--flake-show", help="Include nix flake show output", action="store_true"
    )
    parser.add_argument(
        "-fi", "--flake-info", help="Include nix flake info output", action="store_true"
    )
    parser.add_argument(
        "-hmd", "--header", help="Path to a header markdown file", type=str
    )
    parser.add_argument(
        "-fmd", "--footer", help="Path to a footer markdown file", type=str
    )
    parser.add_argument(
        "-unr",
        "--use-nix-run",
        help="Use nix and github to run the CLI help command, requires an author",
        action="store_true",
    )

    args = parser.parse_args()

    output_file = args.output if args.output else "README.md"
    readme_exists = os.path.exists(output_file)
    readme_content = generate_readme(
        ".",
        args.dir,
        args.links,
        args.flake_show,
        args.flake_info,
        args.header,
        args.footer,
        args.author,
        args.repo,
        include_cli_usage=args.usage,
        use_nix_for_cli=args.use_nix_run,
    )

    with open(output_file, "w") as f:
        f.write(readme_content)

    if readme_exists:
        print(f"{output_file} existed and was overwritten.")
    else:
        print(f"{output_file} did not exist and was created.")
