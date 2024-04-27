{
  description = "Readme generator";


  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        inherit (poetry2nix.lib.mkPoetry2Nix { inherit pkgs; }) mkPoetryApplication overrides;
      in
      {
        packages = {
          readme-py = mkPoetryApplication {
            projectDir = ./.;
            overrides = overrides.withDefaults (self: super: {
              argparse = super.argparse.overridePythonAttrs (
                old: {
                  nativeBuildInputs = (old.nativeBuildInputs or [ ]) ++ [
                    self.setuptools
                  ];
                }
              );
            });
          };
          default = self.packages.${system}.readme-py;
        };

        devShells = {
          default = pkgs.mkShell {
            inputsFrom = [ self.packages.${system}.readme-py ];
            packages = [ pkgs.poetry ];
          };
        };

        formatter = pkgs.nixpkgs-fmt;
      });
}
