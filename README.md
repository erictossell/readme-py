# readme-py

A simple python script to generate a README.md file.

## Example

```bash
readme-py --dir --links --header header.md --nix
```
# readme-py

### Directory Tree

[app](app/)
[test](test/)

### CLI Usage

```bash

```

### Nix Flake Show

```nix
git+file:///home/runner/work/readme-py/readme-py?ref=refs/heads/main&rev=89a5479e63128c97119a3958a9ff46a3ac348788&shallow=1
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
