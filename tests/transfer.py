import csv
import json
import re

def parse_alignment(alignment):
    mapping = {
        'L': 'lawful', 'N': 'neutral', 'C': 'chaotic',
        'G': 'good', 'E': 'evil', 'U': 'unaligned', 'A': 'any'
    }
    if not alignment:
        return "unknown", "unknown"
    alignment = alignment.strip().upper()
    if alignment == 'U':
        return 'unaligned', 'neutral'
    if alignment == 'ANY':
        return 'any', 'any'
    if len(alignment) == 2:
        return mapping.get(alignment[0], 'neutral'), mapping.get(alignment[1], 'neutral')
    elif len(alignment) == 1:
        return mapping.get(alignment[0], 'neutral'), 'neutral'
    return 'neutral', 'neutral'

def extract_first_number(text):
    match = re.search(r'\d+', str(text))
    return int(match.group()) if match else 0

def safe_int(value):
    try:
        return int(value)
    except:
        return 0

# Load CSV
with open('monsters.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    data = {}

    for row in reader:
        name = row['Name']
        size = row['Size'].lower()
        race = row['Type']
        alignment, karma = parse_alignment(row['Align.'])
        armor_class = safe_int(row.get('AC'))
        hit_points = safe_int(row.get('HP'))
        speed = extract_first_number(row.get('Speeds'))

        stats = {
            "STR": safe_int(row.get("STR")),
            "DEX": safe_int(row.get("DEX")),
            "CON": safe_int(row.get("CON")),
            "INT": safe_int(row.get("INT")),
            "WIS": safe_int(row.get("WIS")),
            "CHA": safe_int(row.get("CHA")),
        }

        data[name] = {
            "size": size,
            "race": race,
            "alignment": alignment,
            "karma": karma,
            "armor Class": armor_class,
            "hit Points": hit_points,
            "speed": speed,
            "stat": stats
        }

# Save as JSON
with open('creatures.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print("Zapisano dane do creatures.json")