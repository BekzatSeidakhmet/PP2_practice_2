import json

try:
    # Файлды оқу
    with open('sample-data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Кесте тақырыбы
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
    print("-" * 80)

    # Мәліметтерді шығару
    for item in data.get("imdata", []):
        attr = item.get("l1PhysIf", {}).get("attributes", {})
        dn = attr.get("dn", "")
        descr = attr.get("descr", "")
        speed = attr.get("speed", "inherit")
        mtu = attr.get("mtu", "")
        print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")

except json.JSONDecodeError as e:
    print(f"Қате: JSON файлында синтаксистік қате бар!")
    print(f"Қате мына жерде: Line {e.lineno}, Column {e.colno}")
    print(f"Хабарлама: {e.msg}")
except Exception as e:
    print(f"Күтпеген қате: {e}")
