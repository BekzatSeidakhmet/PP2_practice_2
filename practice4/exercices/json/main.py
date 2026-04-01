import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'sample-data.json')

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
    print("-" * 50 + " " + "-" * 20 + " " + "-" * 7 + " " + "-" * 6)

    for item in data.get("imdata", []):
        attr = item.get("l1PhysIf", {}).get("attributes", {})
        print(f"{attr.get('dn', ''):<50} {attr.get('descr', ''):<20} {attr.get('speed', 'inherit'):<7} {attr.get('mtu', ''):<6}")

except FileNotFoundError:
    print(f"Қате: {file_path} жолы бойынша файл табылмады.")
except json.JSONDecodeError:
    print("Қате: JSON файлының құрылымы дұрыс емес.")
    