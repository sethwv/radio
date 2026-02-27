# Contributing

Pull requests that add or correct CSV files are welcome.

## CSV format

Each CSV must have these columns:

| column | description |
|--------|-------------|
| `section` | Section header label (first row of a group only, e.g. `AM RADIO STREAMS`) |
| `chno` | Channel number — use `10000 + frequency * 10` (e.g. 91.5 FM = `10915`) |
| `title` | `CALLSIGN FREQ` (e.g. `CKGL 570`, `CKBT 91.5`) |
| `group` | Group title (e.g. `RADIO - FM`) |
| `logo` | Logo URL |
| `url` | Stream URL (must be publicly accessible without authentication) |

## File naming

CSV filenames follow the pattern `country-region-city.csv` using short lowercase codes:

- `ca-on-toronto.csv` — Canada, Ontario, Toronto
- `us-mo-stlouis.csv` — US, Missouri, St. Louis
- `ca-sportsnet.csv` — Canada-wide, no region

Keep each segment to 3 characters or fewer (except the city/name). This convention drives the automatic grouped playlist generation.

## Title format

Titles should be `CALLSIGN FREQ` where possible:

- `CKGL 570` (AM)
- `CKBT 91.5` (FM)

Use the station's official callsign without `-FM` or `-AM` suffixes.

## Stream URLs

Only link to streams that are **freely and publicly accessible**. Streams must not require authentication, DRM circumvention, or any form of paywall bypass.

Preferred formats in order:
1. HLS (`.m3u8`)
2. AAC / MP3 direct streams

## Submitting a pull request

1. Add or edit a CSV file on the `main` branch.
2. Make sure the CSV is valid (correct headers, no trailing commas).
3. Open a PR — the workflow will automatically generate the playlist and deploy it once merged.
