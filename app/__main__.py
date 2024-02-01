import subprocess
import os
import re
import argparse


def strip_ansi_sequences(text):
    """Remove ANSI escape sequences from a string."""
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return strip_ansi_sequences(result.stdout)


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


def generate_readme(
    path,
    include_dir_tree,
    include_links,
    include_nix,
    markdown_prefix_file,
    username=None,
    repo_name=None,
):
    existing_content = ""
    if markdown_prefix_file and os.path.exists(markdown_prefix_file):
        with open(markdown_prefix_file, "r") as f:
            existing_content = f.read()

    readme_content = existing_content

    if username and repo_name:
        readme_content += f"\n\n## Repository Information\n**User:** {username}\n**Repository:** {repo_name}\n"

    if include_dir_tree:
        dir_tree = directory_tree(path, make_links=include_links)
        readme_content += (
            "\n\n`Directory Tree`\n\n"
            + ("```bash\n" + dir_tree + "\n```" if not include_links else dir_tree)
            + "\n"
        )

    if include_nix:
        flake_show_output = run_command("nix flake show . --all-systems")
        readme_content += (
            "## Nix Flake Show\n\n```nix\n" + flake_show_output + "\n```\n"
        )

    return readme_content


def main():
    parser = argparse.ArgumentParser(description="Generate README.md content.")
    parser.add_argument(
        "--dir-tree", help="Include directory tree structure", action="store_true"
    )
    parser.add_argument("--header", help="Path to the header markdown file", type=str)
    parser.add_argument(
        "--nix", help="Include nix flake show output", action="store_true"
    )
    parser.add_argument("--username", help="GitHub username", type=str)
    parser.add_argument("--repo-name", help="GitHub repository name", type=str)
    parser.add_argument(
        "--links", help="Turn directory tree into Markdown links", action="store_true"
    )
    args = parser.parse_args()

    readme_exists = os.path.exists("README.md")
    readme_content = generate_readme(
        ".",
        args.dir_tree,
        args.links,
        args.nix,
        args.header,
        args.username,
        args.repo_name,
    )

    with open("README.md", "w") as f:
        f.write(readme_content)

    if readme_exists:
        print("README.md existed and was overwritten.")
    else:
        print("README.md did not exist and was created.")


if __name__ == "__main__":
    main()
