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
| **ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca/playlist.m3u8 | [2026-02-27 22:27 UTC](https://github.com/sethwv/radio-playlists/commit/0135af9f911f3a08a6cbf408d3b696418b1e0982) |
| **ca-bc** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/b23887160409ce75e0dc2df4df44c1dda6251443) |
| [ca-bc-vancouver.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-bc-vancouver.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-bc-vancouver/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/d13b11531a863eb7d2c79e94cc3b8849d86da87d) |
| **ca-on** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on/playlist.m3u8 | [2026-02-27 22:27 UTC](https://github.com/sethwv/radio-playlists/commit/81f4faddc58371de988bcdaa88b5a27b023e2898) |
| [ca-on-barrie.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-barrie.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-barrie/playlist.m3u8 | [2026-02-27 22:27 UTC](https://github.com/sethwv/radio-playlists/commit/7ee7f81b86dc4b72d93c92100d6070c40c436c7b) |
| [ca-on-collingwood.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-collingwood.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-collingwood/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/1abb6d7452e4a31357290f1e78c6070d2c4ffb8a) |
| [ca-on-kitchener.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-kitchener.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-kitchener/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/f75f88a745565eebdd0b20aa4e84be60093cee29) |
| [ca-on-toronto.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-toronto.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-toronto/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/c9308343fd3159fced1734dee5ee530a72ba45ac) |
| [ca-sportsnet.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sportsnet.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-sportsnet/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/532fa0dad531b24e5e4bb91a842f3985c8160730) |
| **us** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/31beeb94ebef01087e1d4109fa63d584c383f45f) |
| **us-ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/7c8492015532d7c5a1a2a2895d013cd356e9e1fe) |
| [us-ca-sanfancisco.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ca-sanfancisco.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ca-sanfancisco/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/e08afa5114d56a0f2f8ab93dd96290a5a9928a32) |
| **us-mo** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/47279b5cca337b227335bd54d374c089e80df3c8) |
| [us-mo-stlouis.csv](https://github.com/sethwv/radio-playlists/blob/main/us-mo-stlouis.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo-stlouis/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/02455047a0adfa9075bfcb9929c97f9205772dfb) |
| **us-ny** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/8ecf780173d9418aae18316dd408ab9bbf09abab) |
| [us-ny-newyork.csv](https://github.com/sethwv/radio-playlists/blob/main/us-ny-newyork.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-ny-newyork/playlist.m3u8 | [2026-02-27 18:59 UTC](https://github.com/sethwv/radio-playlists/commit/0fcfb81fa8f25a2985bdda1b9426057db6f65a6b) |
