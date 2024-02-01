

### Directory Tree

[app](app/)
[test](test/)

### CLI Usage

```bash
usage: readme-py [-h] [--dir] [--header HEADER] [--flake-show]
                 [--author AUTHOR] [--title TITLE] [--links] [--usage]
                 [--use-nix-build]

Generate README.md content.

options:
  -h, --help       show this help message and exit
  --dir            Include directory tree structure
  --header HEADER  Path to the header markdown file
  --flake-show     Include nix flake show output
  --author AUTHOR  GitHub username
  --title TITLE    GitHub repository name
  --links          Turn directory tree into Markdown links
  --usage          Include CLI application usage
  --use-nix-build  Use nix to run the CLI help command

```

### Nix Flake Show

```nix
git+file:///home/runner/work/readme-py/readme-py?ref=refs/heads/main&rev=ff915bb266f71b92254c2a89ccf467748ea57d0a&shallow=1
├───devShells
│   ├───aarch64-darwin
│   │   └───default: development environment 'nix-shell'
│   ├───aarch64-linux
│   │   └───default: development environment 'nix-shell'
│   ├───x86_64-darwin
│   │   └───default: development environment 'nix-shell'
│   └───x86_64-linux
│       └───default: development environment 'nix-shell'
├───formatter
│   ├───aarch64-darwin: package 'nixpkgs-fmt-1.3.0'
│   ├───aarch64-linux: package 'nixpkgs-fmt-1.3.0'
│   ├───x86_64-darwin: package 'nixpkgs-fmt-1.3.0'
│   └───x86_64-linux: package 'nixpkgs-fmt-1.3.0'
└───packages
    ├───aarch64-darwin
    │   ├───default: package 'python3.11-readme-py-0.1.0'
    │   └───readme-py: package 'python3.11-readme-py-0.1.0'
    ├───aarch64-linux
    │   ├───default: package 'python3.11-readme-py-0.1.0'
    │   └───readme-py: package 'python3.11-readme-py-0.1.0'
    ├───x86_64-darwin
    │   ├───default: package 'python3.11-readme-py-0.1.0'
    │   └───readme-py: package 'python3.11-readme-py-0.1.0'
    └───x86_64-linux
        ├───default: package 'python3.11-readme-py-0.1.0'
        └───readme-py: package 'python3.11-readme-py-0.1.0'

```
