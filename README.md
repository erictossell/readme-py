# readme-py

A simple `python` script to generate a `README.md` file. Expose your project's structure and `cli` usage in a programmatic way.

Easy to use in github actions, `nix` derivations, or any other `nix` build system.

## Example

```bash
readme-py --dir --links --flake-show --header header.md --footer footer.md
```
# readme-py

### Directory Tree

[app](app/)
[test](test/)

### CLI Usage

```bash
usage: readme-py [-h] [-d] [-hmd HEADER] [-fmd FOOTER] [-fs] [-fi] [-a AUTHOR]
                 [-r REPO] [-l] [-u] [-unr] [-o OUTPUT]

Generate README.md content.

options:
  -h, --help            show this help message and exit
  -d, --dir             Include directory tree structure
  -hmd HEADER, --header HEADER
                        Path to the header markdown file
  -fmd FOOTER, --footer FOOTER
                        Path to the footer markdown file
  -fs, --flake-show     Include nix flake show output
  -fi, --flake-info     Include nix flake info output
  -a AUTHOR, --author AUTHOR
                        GitHub username
  -r REPO, --repo REPO  GitHub repository name
  -l, --links           Turn directory tree into Markdown links
  -u, --usage           Include CLI application usage
  -unr, --use-nix-run   Use nix to run the CLI help command, requires an
                        author
  -o OUTPUT, --output OUTPUT
                        Output file to write to

```

### Nix Flake Info

```nix
Resolved URL:  git+file:///home/eriim/repos/py/readme-py
Locked URL:    git+file:///home/eriim/repos/py/readme-py
Description:   Readme generator
Path:          /nix/store/ilg7mlxdxw5v0mnhrj8d9ynm6vi4mzz9-source
Revision:      c05f3846bc5d4735904e1aab3fea0271328783dd-dirty
Last modified: 2024-02-01 22:13:37
Inputs:
├───flake-utils: github:numtide/flake-utils/1ef2e671c3b0c19053962c07dbda38332dcebf26
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───nixpkgs: github:NixOS/nixpkgs/97b17f32362e475016f942bbdfda4a4a72a8a652
└───poetry2nix: github:nix-community/poetry2nix/e0b44e9e2d3aa855d1dd77b06f067cd0e0c3860d
    ├───flake-utils: github:numtide/flake-utils/ff7b65b44d01cf9ba6a71320833626af21126384
    │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
    ├───nix-github-actions: github:nix-community/nix-github-actions/4bb5e752616262457bc7ca5882192a564c0472d2
    │   └───nixpkgs follows input 'poetry2nix/nixpkgs'
    ├───nixpkgs follows input 'nixpkgs'
    ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
    └───treefmt-nix: github:numtide/treefmt-nix/e82f32aa7f06bbbd56d7b12186d555223dc399d1
        └───nixpkgs follows input 'poetry2nix/nixpkgs'

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

---

👤 [**erictossell**](https://github.com/erictossell)

[![Flake Check](https://github.com/erictossell/readme-py/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/check.yml)
[![Flake Update](https://github.com/erictossell/readme-py/actions/workflows/update.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/update.yml)
[![Readme Update](https://github.com/erictossell/readme-py/actions/workflows/readme.yml/badge.svg)](https://github.com/erictossell/readme-py/actions/workflows/readme.yml)
