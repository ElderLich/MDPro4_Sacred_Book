import json
import re

# ✅ Divine-Beast card names and IDs
names = {
    10000000: "Obelisk the Tormentor",
    10000020: "Slifer the Sky Dragon",
    10000010: "The Winged Dragon of Ra",
    10000080: "The Winged Dragon of Ra - Sphere Mode",
    10000090: "The Winged Dragon of Ra - Immortal Phoenix"
}

# 🔃 Load the full merged JSON file
with open("merged_cards.json", encoding="utf-8") as f:
    cards = json.load(f)

mentions = {}

for card in cards:
    if 'desc' not in card or not card['desc']:
        continue
    mentioned = []
    for id, name in names.items():
        if name in card['desc']:
            mentioned.append(id)
    if mentioned:
        mentions[card['id']] = mentioned

# 🧾 Output Lua table
print("local mentions = {")
for cid, mids in sorted(mentions.items()):
    print(f"    [{cid}] = {{{', '.join(str(mid) for mid in mids)}}},")
print("}")
