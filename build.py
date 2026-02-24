#!/usr/bin/env python3
"""Generate a playlist.m3u8 from a stations CSV file.

Usage: python3 build.py [stations.csv]
"""

import csv
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
OUTPUT_FILE = SCRIPT_DIR / "playlist.m3u8"

def build_extinf(chno, logo, group, title):
    callsign = title.split()[0]
    tvg_id = f"{chno}-{callsign}"
    return (
        f'#EXTINF:-1 tvg-chno="{chno}" tvg-id="{tvg_id}"'
        f' tvg-logo="{logo}"'
        f' group-title="{group}",{title}'
    )

def main():
    csv_file = Path(sys.argv[1]) if len(sys.argv) > 1 else SCRIPT_DIR / "stations.csv"

    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        lines = ["#EXTM3U"]
        current_section = None

        for row in reader:
            section  = row["section"].strip()
            chno     = row["chno"].strip()
            logo     = row["logo"].strip()
            group    = row["group"].strip()
            title    = row["title"].strip()
            url      = row["url"].strip()

            if section and section != current_section:
                current_section = section
                bar = "=" * 67
                lines += [
                    "",
                    f"# {bar}",
                    f"# {section}",
                    f"# {bar}",
                    "",
                ]

            lines.append(f"# {title}")
            lines.append(build_extinf(chno, logo, group, title))
            lines.append(url)
            lines.append("")

    output = "\n".join(lines).rstrip("\n") + "\n"
    with open(OUTPUT_FILE, "w") as out:
        out.write(output)
    print(f"{csv_file.name} → {OUTPUT_FILE.name}")

if __name__ == "__main__":
    main()
