# readme-py

A simple `python` script to generate a `README.md` file. Expose your project's structure and `cli` usage in a programmatic way.

Easy to use in github actions, `nix` derivations, or any other `nix` build system.

This repo's `README.md` was generated with `readme-py` and `github-actions`. Check out the the simple [`readme.yml`](.github/workflows/readme.yml).

## Example

```bash
readme-py --dir --links --flake-show --header header.md --footer footer.md
```

An example generation of a `README.md` can be generated with the following command:

```bash
nix run github:erictossell/readme-py -- --output TEST.md --author erictossell --repo readme-py --dir --links --usage --flake-info --flake-show --header header.md --footer footer.md
```

### Directory

[app](app/)

[test](test/)


### Usage

```bash
usage: readme-py [-h] [-a AUTHOR] [-r REPO] [-o OUTPUT] [-d] [-l] [-u] [-fs]
                 [-fi] [-hmd HEADER] [-fmd FOOTER] [-unr]

Generate README.md content.

options:
  -h, --help            show this help message and exit
  -a AUTHOR, --author AUTHOR
                        GitHub username
  -r REPO, --repo REPO  GitHub repository name
  -o OUTPUT, --output OUTPUT
                        Output file to write to, defaults to README.md
  -d, --dir             Include directory tree structure
  -l, --links           Turn directory tree into Markdown links
  -u, --usage           Include CLI application usage by building with nix
  -fs, --flake-show     Include nix flake show output
  -fi, --flake-info     Include nix flake info output
  -hmd HEADER, --header HEADER
                        Path to a header markdown file
  -fmd FOOTER, --footer FOOTER
                        Path to a footer markdown file
  -unr, --use-nix-run   Use nix and github to run the CLI help command,
                        requires an author

```

### Flake Info

```nix
Resolved URL:  git+file:///home/eriim/repos/py/readme-py
Locked URL:    git+file:///home/eriim/repos/py/readme-py?ref=refs/heads/main&rev=38bff41c052f10a3f1f59e87e09a894390fc2b8d
Description:   Readme generator
Path:          /nix/store/9q7f5c0cwd2izs3kg8k8lgj68najgc1n-source
Revision:      38bff41c052f10a3f1f59e87e09a894390fc2b8d
Revisions:     43
Last modified: 2024-02-01 23:09:07
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

### Flake Outputs

```nix
git+file:///home/eriim/repos/py/readme-py?ref=refs/heads/main&rev=38bff41c052f10a3f1f59e87e09a894390fc2b8d
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
