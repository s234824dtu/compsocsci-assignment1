#!/usr/bin/env python3

import csv
import pickle

names = set()
with open("ic2s2_2025_schedule_v5.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["type"] == "session_presentation" and "poster" in row.get("session", "").lower():
            for name in row["author"].split(", "):
                name = name.strip()
                if name:
                    names.add(name)

names = sorted(names)

with open("poster_authors.pkl", "wb") as f:
    pickle.dump(names, f)
