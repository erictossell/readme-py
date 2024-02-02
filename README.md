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

### Flake Outputs

```nix
git+file:///home/runner/work/readme-py/readme-py?ref=refs/heads/main&rev=0521b3960f74004d0794f376456b7a1f149398c5&shallow=1
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
[![Python Tests](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/erictossell/readme-py/actions/workflows/pytest.yml)
