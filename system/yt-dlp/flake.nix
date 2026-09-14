{
  description = "A ephemeral environment for yt-dlp on NixOS unstable";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      # Change system to "aarch64-linux" if on ARM64
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      # Run directly with `nix run`
      apps.${system}.default = {
        type = "app";
        program = "${pkgs.yt-dlp}/bin/yt-dlp";
      };

      # Enter shell with `nix develop`
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.yt-dlp
          pkgs.ffmpeg # Included for video merging/post-processing
        ];
      };
    };
}
