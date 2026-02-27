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
| **ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/dc644b06bccb8b7fbde0c005523689446de22656) |
| **ca-bc** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/f5335f659ea11e612e2f21d7b1cb14187424a697) |
| [ca-bc-vancouver.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-bc-vancouver.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc-vancouver/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/65ea0c3f0746b7a010147466c27c4f5412cf45f2) |
| **ca-on** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/7f38e388d9b3eeccbb5b4bb4451a6ddc905134fd) |
| [ca-on-collingwood.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-collingwood.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-collingwood/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/16642bc70900e5f1085e3a2f8d0c8b5dd92f8a0d) |
| [ca-on-kitchener.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-kitchener.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-kitchener/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/5b8954f690c314a755b9b67e2eb03df51954d981) |
| [ca-on-toronto.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-toronto.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-toronto/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/f81df2cf0a8e557bc34407e8e3cc2b699901c22c) |
| [ca-sportsnet.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sportsnet.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-sportsnet/playlist.m3u8 | [2026-02-27 18:20 UTC](https://github.com/sethwv/radio-playlists/commit/9a645376642e3dae4140fbf63b0a28ba8d7948fc) |
| **us** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/002844b434ea7b3ad008ef288e56ab69594d2205) |
| **us-ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/748499b88772d4f2b301bc484ecead73419521f4) |
| [us-ca-sanfancisco.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ca-sanfancisco.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca-sanfancisco/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/2d74ffd88aeecff542cb68cb73bd56174d24b084) |
| **us-mo** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/c71750b40beb3df0edf140788ea883c1dc2d5f89) |
| [us-mo-stlouis.csv](https://github.com/sethwv/radio-playlists/blob/main/us-mo-stlouis.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo-stlouis/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/1e40d14382bc8f8797a8757c58430b35c40f198a) |
| **us-ny** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/fc247c731c3432039a170d2cf8a4ff9292b7553d) |
| [us-ny-newyork.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ny-newyork.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny-newyork/playlist.m3u8 | [2026-02-27 18:49 UTC](https://github.com/sethwv/radio-playlists/commit/32d81967247972cc208760e269cee34252dbeabc) |
