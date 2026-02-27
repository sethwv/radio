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
| **ca** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca/playlist.m3u8 | [2026-02-27 17:37 UTC](https://github.com/sethwv/radio-playlists/commit/be4a372e405b6478667a4a3c15c68da9bbe04936) |
| **ca-on** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on/playlist.m3u8 | [2026-02-27 17:37 UTC](https://github.com/sethwv/radio-playlists/commit/e4074ff0dff3fee3117570785995364399bb5450) |
| [ca-on-collingwood.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-collingwood.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-collingwood/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/3d89f71f8deb60d010df28f5298ddc42cae19b81) |
| [ca-on-kitchener.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-kitchener.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-kitchener/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/bbfb15e22663e32035cc91356ab90397fef92c52) |
| [ca-on-toronto.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-on-toronto.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-on-toronto/playlist.m3u8 | [2026-02-27 17:37 UTC](https://github.com/sethwv/radio-playlists/commit/9068f5a9741e7c69732fc36054086d9a749bd468) |
| [ca-sportsnet.csv](https://github.com/sethwv/radio-playlists/blob/main/ca-sportsnet.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/ca-sportsnet/playlist.m3u8 | [2026-02-27 17:37 UTC](https://github.com/sethwv/radio-playlists/commit/03c6fdd7c447a2409cfc4b45d5b512ee8ed2e52e) |
| **us** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/6c138bfbf869856b22dd0f5b0c2f1f1168fa2b1e) |
| **us-mo** | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/ec1038112b1f0f514ce7c46fe2248a61d9fafa30) |
| [us-mo-stlouis.csv](https://github.com/sethwv/radio-playlists/blob/main/us-mo-stlouis.csv) | https://raw.githubusercontent.com/sethwv/radio-playlists/refs/heads/us-mo-stlouis/playlist.m3u8 | [2026-02-27 17:26 UTC](https://github.com/sethwv/radio-playlists/commit/c11ba2207e148b5e2f9eafa3a26831e71650ea62) |
