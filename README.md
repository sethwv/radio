# radio-playlists
## Disclaimer

This repository contains only links to streams that are **freely and publicly accessible** without authentication, DRM circumvention, or any form of paywall bypass. All streams are broadcast by licensed radio stations for public reception. No audio content is hosted, reproduced, or redistributed here.

Use of these streams is subject to the terms of the respective broadcasters and applicable laws in your jurisdiction. This project is intended for personal, non-commercial use only.

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
| [ca-sw-ontario.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sw-ontario.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/ca-sw-ontario/playlist.m3u8 | [2026-02-24 20:49 UTC](https://github.com/sethwv/radio-playlists/commit/70900f2cde50dbd89f0c10151d420918904fe753) |
| [example.csv](https://github.com/sethwv/radio-playlists/blob/main/example.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/example/playlist.m3u8 | [2026-02-24 21:11 UTC](https://github.com/sethwv/radio-playlists/commit/cda6bb6befe21a21fe2c6247b4affc4cd7039d48) |
