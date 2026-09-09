#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splices the 8 new case-study dicts into generator/gen_lesson10.py's `cases = [...]`
list, and updates the surrounding copy (case count, EuroHomes note).
Run this ON THE DEVICE from the repo root:
    python3 splice.py
It reads generator/gen_lesson10.py and new_cases.py (both expected in the
same directory as this script, or pass paths as argv[1] / argv[2]), and
overwrites generator/gen_lesson10.py in place.
"""
import sys
import re
import os

repo_gen = sys.argv[1] if len(sys.argv) > 1 else "generator/gen_lesson10.py"
new_cases_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_cases.py")

with open(repo_gen, "r", encoding="utf-8") as f:
    src = f.read()

ns = {}
with open(new_cases_path, "r", encoding="utf-8") as f:
    exec(f.read(), ns)
new_cases_source = ns["NEW_CASES_SOURCE"]

# 1. Splice the new case dicts into the cases list, right before the closing "]"
marker = "  )),\n]\n"
assert src.count(marker) == 1, f"marker occurrence count = {src.count(marker)}, expected 1"
replacement = "  )),\n" + new_cases_source.strip("\n") + "\n]\n"
src2 = src.replace(marker, replacement, 1)
assert src2 != src, "cases list splice did not change anything"

# 2. Update section title "9 кейсов" -> "17 кейсов"
old_title = 'sec_cases = section("cases", "9 кейсов"'
new_title = 'sec_cases = section("cases", "17 кейсов"'
assert src2.count(old_title) == 1
src2 = src2.replace(old_title, new_title, 1)

# 3. Update page() desc: "9 полных ролевых кейсов" -> "17 полных ролевых кейсов"
old_desc = "9 полных ролевых кейсов"
new_desc = "17 полных ролевых кейсов"
assert src2.count(old_desc) == 1, f"desc occurrence = {src2.count(old_desc)}"
src2 = src2.replace(old_desc, new_desc, 1)

# 4. Remove/update the note about EuroHomes/lesson10 being incomplete
old_note = '<div class="note">В изначном материале 10 кейсов — десятый (Real Estate · EuroHomes) присланы не полностью, добавим отдельно, когда будет весь текст.</div>'
new_note = '<div class="note">17 полных ролевых кейсов — от SaaS и Local SEO до fintech, iGaming, health, travel, legal и crypto. Три кейса (15–17) помечены Reserve — для отработки Reddit/LLM-visibility тем.</div>'
assert src2.count(old_note) == 1, f"note occurrence = {src2.count(old_note)}"
src2 = src2.replace(old_note, new_note, 1)

with open(repo_gen, "w", encoding="utf-8") as f:
    f.write(src2)

print("OK: spliced 8 new cases, updated title/desc/note.")
