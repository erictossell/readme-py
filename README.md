# readme-py

A simple python script to generate a README.md file.

## Example

```bash
readme-py --dir --links --header header.md --nix
```


### Directory Tree

[app](app/)

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
git+file:///home/eriim/repos/py/readme-py
├───devShells
│   ├───aarch64-darwin
│   │   └───default: development environment 'nix-shell'
│   ├───aarch64-linux
│   │   └───default: development environment 'nix-shell'
│   ├───x86_64-darwin
│   │   └───default: development environment 'nix-shell'
│   └───x86_64-linux
│       └───default: development environment 'nix-shell'
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
