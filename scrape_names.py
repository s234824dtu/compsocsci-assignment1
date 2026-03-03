#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

URL = "https://ic2s2-2025.org/organization/"

resp = requests.get(URL)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")
FOOTER_HEADINGS = {"Address", "Social", "Email"}
people = set()
for center in soup.find_all("center"):
    h3 = center.find("h3")
    if not h3 or h3.get_text(strip=True) in FOOTER_HEADINGS:
        continue

    name = h3.get_text(strip=True)
    people.add(name)

print(list(people))
