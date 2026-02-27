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
| **ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca/playlist.m3u8 | [2026-02-27 18:20 UTC](https://github.com/sethwv/radio-playlists/commit/25d0a4c09d18a8ad566bba135bef13f0da4ff503) |
| **ca-bc** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc/playlist.m3u8 | [2026-02-27 18:04 UTC](https://github.com/sethwv/radio-playlists/commit/5dc9c480d106d12c34493e08431bb3f0850c8bbe) |
| [ca-bc-vancouver.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-bc-vancouver.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc-vancouver/playlist.m3u8 | [2026-02-27 18:03 UTC](https://github.com/sethwv/radio-playlists/commit/6b7e49aeae2663d50e5fbee5f612511c6dce1e0e) |
| **ca-on** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on/playlist.m3u8 | [2026-02-27 17:45 UTC](https://github.com/sethwv/radio-playlists/commit/8e96c5c3e44e4375db50d6f733095c1bccd6ea5e) |
| [ca-on-collingwood.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-collingwood.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-collingwood/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/3d89f71f8deb60d010df28f5298ddc42cae19b81) |
| [ca-on-kitchener.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-kitchener.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-kitchener/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/bbfb15e22663e32035cc91356ab90397fef92c52) |
| [ca-on-toronto.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-toronto.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-toronto/playlist.m3u8 | [2026-02-27 17:44 UTC](https://github.com/sethwv/radio-playlists/commit/3a5d40d8fa5f3ba07d3caebd4a8d3cfee5379dda) |
| [ca-sportsnet.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sportsnet.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-sportsnet/playlist.m3u8 | [2026-02-27 18:20 UTC](https://github.com/sethwv/radio-playlists/commit/9a645376642e3dae4140fbf63b0a28ba8d7948fc) |
| **us** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us/playlist.m3u8 | [2026-02-27 18:04 UTC](https://github.com/sethwv/radio-playlists/commit/27f37119e83ffbb1106ba4d89663bf633b406b62) |
| **us-ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca/playlist.m3u8 | [2026-02-27 18:04 UTC](https://github.com/sethwv/radio-playlists/commit/ea464102b171369a7426ddd04ec2f6d7c9ffc4ef) |
| [us-ca-sanfancisco.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ca-sanfancisco.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca-sanfancisco/playlist.m3u8 | [2026-02-27 18:03 UTC](https://github.com/sethwv/radio-playlists/commit/d7665cfb16277026d654840cf7bd701f01f07495) |
| **us-mo** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/ec1038112b1f0f514ce7c46fe2248a61d9fafa30) |
| [us-mo-stlouis.csv](https://github.com/sethwv/radio-playlists/blob/main/us-mo-stlouis.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo-stlouis/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/c11ba2207e148b5e2f9eafa3a26831e71650ea62) |
| **us-ny** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny/playlist.m3u8 | [2026-02-27 18:04 UTC](https://github.com/sethwv/radio-playlists/commit/aa9674e51505248e079118e23d193b9f09fa6286) |
| [us-ny-newyork.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ny-newyork.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny-newyork/playlist.m3u8 | [2026-02-27 18:03 UTC](https://github.com/sethwv/radio-playlists/commit/d09d3fe661f4ad77d9d76f332d5ef1267e727964) |
