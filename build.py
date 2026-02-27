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

    # First pass: group all stations by section
    from collections import OrderedDict
    sections = OrderedDict()
    current_section = None
    
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            section  = row["section"].strip()
            chno     = row["chno"].strip()
            logo     = row["logo"].strip()
            group    = row["group"].strip()
            title    = row["title"].strip()
            url      = row["url"].strip()

            # Update current section if this row specifies one
            if section:
                current_section = section
                if current_section not in sections:
                    sections[current_section] = []
            
            # Add station to current section
            if current_section:
                sections[current_section].append({
                    'chno': chno,
                    'logo': logo,
                    'group': group,
                    'title': title,
                    'url': url
                })

    # Deduplicate channel numbers across all sections.
    # First occurrence keeps the original chno; subsequent duplicates
    # get .1, .2, .3, etc. appended.
    chno_counts = {}
    all_stations = [(sec, st) for sec in sections for st in sections[sec]]
    for _sec, station in all_stations:
        base = station['chno']
        if base in chno_counts:
            chno_counts[base] += 1
            station['chno'] = f"{base}.{chno_counts[base]}"
        else:
            chno_counts[base] = 0

    # Second pass: output grouped by section
    lines = ["#EXTM3U"]
    
    for section, stations in sections.items():
        bar = "=" * 67
        lines += [
            "",
            f"# {bar}",
            f"# {section}",
            f"# {bar}",
            "",
        ]
        
        for station in stations:
            lines.append(f"# {station['title']}")
            lines.append(build_extinf(station['chno'], station['logo'], 
                                     station['group'], station['title']))
            lines.append(station['url'])
            lines.append("")

    output = "\n".join(lines).rstrip("\n") + "\n"
    with open(OUTPUT_FILE, "w") as out:
        out.write(output)
    print(f"{csv_file.name} → {OUTPUT_FILE.name}")

if __name__ == "__main__":
    main()
