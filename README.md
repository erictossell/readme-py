# readme-py

[![Flake Check](https://github.com/erictossell/readme-py/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/check.yml)
[![Flake Update](https://github.com/erictossell/readme-py/actions/workflows/update.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/update.yml)
[![Readme Update](https://github.com/erictossell/readme-py/actions/workflows/readme.yml/badge.svg)](https://github.com/erictossell/readme-py/actions/workflows/readme.yml)
[![Python Tests](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml)

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

### Directory Structure

- [app/](app/)
- [test/](test/)

### Usage

```
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
  -unr, --use-nix-run   Use nix and GitHub to run the CLI help command,
                        requires an author

```

### Flake Info

```nix
Resolved URL:  git+file:///home/runner/work/readme-py/readme-py?shallow=1
Locked URL:    git+file:///home/runner/work/readme-py/readme-py?ref=refs/heads/main&rev=8fba8b0fb3d3fb6cc5d21b4965653ccdcd860215&shallow=1
Description:   Readme generator
Path:          /nix/store/i6i1yiazpacpcyn1bnr3sl0wb8i7wf4c-source
Revision:      8fba8b0fb3d3fb6cc5d21b4965653ccdcd860215
Last modified: 2025-03-02 00:14:18
Inputs:
├───flake-utils: github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b
│   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
├───nixpkgs: github:NixOS/nixpkgs/6313551cd05425cd5b3e63fe47dbc324eabb15e4
└───poetry2nix: github:nix-community/poetry2nix/d90f9db68a4bda31c346be16dfd8d3263be4547e
    ├───flake-utils: github:numtide/flake-utils/c1dfcf08411b08f6b8615f7d8971a2bfa81d5e8a
    │   └───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
    ├───nix-github-actions: github:nix-community/nix-github-actions/e04df33f62cdcf93d73e9a04142464753a16db67
    │   └───nixpkgs follows input 'poetry2nix/nixpkgs'
    ├───nixpkgs follows input 'nixpkgs'
    ├───systems: github:nix-systems/default/da67096a3b9bf56a91d16901293e51ba5b49a27e
    └───treefmt-nix: github:numtide/treefmt-nix/9ef337e492a5555d8e17a51c911ff1f02635be15
        └───nixpkgs follows input 'poetry2nix/nixpkgs'

```

### Flake Outputs

```nix
git+file:///home/runner/work/readme-py/readme-py?ref=refs/heads/main&rev=8fba8b0fb3d3fb6cc5d21b4965653ccdcd860215&shallow=1
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
    │   ├───default: package 'python3.12-readme-py-0.1.0'
    │   └───readme-py: package 'python3.12-readme-py-0.1.0'
    ├───aarch64-linux
    │   ├───default: package 'python3.12-readme-py-0.1.0'
    │   └───readme-py: package 'python3.12-readme-py-0.1.0'
    ├───x86_64-darwin
    │   ├───default: package 'python3.12-readme-py-0.1.0'
    │   └───readme-py: package 'python3.12-readme-py-0.1.0'
    └───x86_64-linux
        ├───default: package 'python3.12-readme-py-0.1.0'
        └───readme-py: package 'python3.12-readme-py-0.1.0'

```

---

👤 [**erictossell**](https://github.com/erictossell)

[![Flake Check](https://github.com/erictossell/readme-py/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/check.yml)
[![Flake Update](https://github.com/erictossell/readme-py/actions/workflows/update.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/update.yml)
[![Readme Update](https://github.com/erictossell/readme-py/actions/workflows/readme.yml/badge.svg)](https://github.com/erictossell/readme-py/actions/workflows/readme.yml)
[![Python Tests](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml)
