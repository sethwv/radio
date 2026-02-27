# radio-playlists
## Disclaimer

This repository contains only links to streams that are **freely and publicly accessible** without authentication, DRM circumvention, or any form of paywall bypass. All streams are broadcast by licensed radio stations for public reception. No audio content is hosted, reproduced, or redistributed here.

Use of these streams is subject to the terms of the respective broadcasters and applicable laws in your jurisdiction. This project is intended for personal, non-commercial use only.

## Contributing

Pull requests that add or update CSV files are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

Found a problem or have a suggestion? Open an issue:

- [Report a Broken Link](https://github.com/sethwv/radio-playlists/issues/new?template=broken-link.yml)
- [Report a Broken Logo](https://github.com/sethwv/radio-playlists/issues/new?template=broken-logo.yml)
- [Report Incorrect Info](https://github.com/sethwv/radio-playlists/issues/new?template=incorrect-info.yml)
- [Request a Station](https://github.com/sethwv/radio-playlists/issues/new?template=station-request.yml)
- [Request a Region](https://github.com/sethwv/radio-playlists/issues/new?template=region-request.yml)

## Usage

Playlists are generated from CSV source files and published to per-csv-file branches. The `main` branch contains only the source CSV files, each named `<name>.csv`. The workflow generates a `playlist.m3u8` file for each CSV and commits it to a branch named `<name>`.

### Adding or editing stations

Edit or create a `<name>.csv` file on `main`. Pushing the change triggers the workflow, which generates `playlist.m3u8` and commits it to the `<name>` branch.

CSV format:

| column | description |
|--------|-------------|
| `section` | Section header label (first row of a group only) |
| `chno` | Channel number (`tvg-chno`) |
| `title` | Display name — first word used as callsign for `tvg-id` |
| `group` | Group title (e.g. `RADIO - FM`) |
| `logo` | Logo URL (`tvg-logo`) |
| `url` | Stream URL |

## Playlists

<!-- AUTO-GENERATED: Do not edit below this line -->

| CSV | Playlist | Updated |
|-----|----------|---------|
| **ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/3edb9aea043882609b20b923244ca89771eba015) |
| **ca-bc** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/1a5cedec0b4880f276e44bc3e3d09930446c501e) |
| [ca-bc-vancouver.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-bc-vancouver.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc-vancouver/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/962ad2d29f1f6a34cb7b17b0cd66e4044fa4cfd7) |
| **ca-on** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/da8780174414a198a810121ada167ce6c4c02127) |
| [ca-on-collingwood.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-collingwood.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-collingwood/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/3d89f71f8deb60d010df28f5298ddc42cae19b81) |
| [ca-on-kitchener.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-kitchener.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-kitchener/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/bbfb15e22663e32035cc91356ab90397fef92c52) |
| [ca-on-toronto.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-toronto.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-toronto/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/50ff4bca6b0d771ded80f861b7329e242d315dac) |
| [ca-sportsnet.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sportsnet.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-sportsnet/playlist.m3u8 | [2026-02-27 18:20 UTC](https://github.com/sethwv/radio-playlists/commit/9a645376642e3dae4140fbf63b0a28ba8d7948fc) |
| **us** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/562c67f5dd3e53b520820ae197868516a381647a) |
| **us-ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/20b05c25ae1483be9f48bdf33f1692966ab507a8) |
| [us-ca-sanfancisco.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ca-sanfancisco.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca-sanfancisco/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/65801110ecf25f8f5804a41097bbedc0cd5232b5) |
| **us-mo** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/317f6126006caea8c116e01706a9116fa55c321b) |
| [us-mo-stlouis.csv](https://github.com/sethwv/radio-playlists/blob/main/us-mo-stlouis.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo-stlouis/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/0448ef3163c73a5c629f680ce174eec770feb2b3) |
| **us-ny** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/b7dbfd212ac19fcf9308eaa8ce1b997efde0312e) |
| [us-ny-newyork.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ny-newyork.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny-newyork/playlist.m3u8 | [2026-02-27 18:36 UTC](https://github.com/sethwv/radio-playlists/commit/13a771f8e0e58cb3bac13f9be896607402f805bd) |
