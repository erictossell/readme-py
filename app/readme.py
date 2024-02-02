import re
import os
import subprocess
import argparse
import sys


def strip_ansi_sequences(text):
    """Remove ANSI escape sequences from a string."""
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def run_command(command):
    """Run a shell command and return its output, handling errors separately."""
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        return strip_ansi_sequences(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return None


def capture_cli_usage(project_root, repo_name, author, use_nix=False):
    """Dynamically determine and run the `--help` command for the project."""
    if use_nix:
        command = ["nix", "run", f"github:{author}/{repo_name}", "--", "--help"]
    else:
        command = [os.path.join(project_root, f"result/bin/{repo_name}"), "--help"]
    return run_command(command)


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
        indent = "    " * level  # Using spaces for indentation
        dir_name = os.path.basename(dir)
        dir_path = os.path.relpath(dir, path) if make_links else ""
        tree.append(
            f"{indent}[{dir_name}]({dir_path}/)\n"
            if make_links
            else f"{indent}{dir_name}/\n"
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
    """Generate README content based on the provided arguments."""
    existing_content = ""
    if markdown_prefix_file and os.path.exists(markdown_prefix_file):
        with open(markdown_prefix_file, "r") as f:
            existing_content += f.read()

    readme_content = existing_content + (f"# {repo_name}\n" if repo_name else "")

    if include_dir_tree:
        dir_tree = directory_tree(path, make_links=include_links)
        readme_content += f"\n### Directory Structure\n\n{dir_tree}\n"

    if include_cli_usage:
        cli_usage_output = capture_cli_usage(
            path, repo_name or get_repo_name(), author, use_nix_for_cli
        )
        readme_content += f"\n### Usage\n\n```\n{cli_usage_output}\n```\n"

    if include_flake_info:
        flake_info_output = run_command(["nix", "flake", "info", "."])
        readme_content += f"\n### Flake Info\n\n```nix\n{flake_info_output}\n```\n"

    if include_flake_show:
        flake_show_output = run_command(["nix", "flake", "show", ".", "--all-systems"])
        readme_content += f"\n### Flake Outputs\n\n```nix\n{flake_show_output}\n```\n"

    if author:
        readme_content += f"\n---\n\n👤 [**{author}**](https://github.com/{author})\n"

    if markdown_footer_file and os.path.exists(markdown_footer_file):
        with open(markdown_footer_file, "r") as f:
            readme_content += "\n" + f.read()

    return readme_content


def write_readme(output_file, content):
    """Write the generated README content to the specified file."""
    with open(output_file, "w") as f:
        f.write(content)
    print(f"README file '{output_file}' generated.")


def parse_arguments():
    """Parse command line arguments."""
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
        help="Use nix and GitHub to run the CLI help command, requires an author",
        action="store_true",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
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
    write_readme(args.output, readme_content)
