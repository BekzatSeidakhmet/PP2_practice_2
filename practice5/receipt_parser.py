import re
import json

# Читаем файл
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1️⃣ Extract prices
prices = re.findall(r"\d+\.\d{2}", text)
prices = [float(p) for p in prices]

# 2️⃣ Extract product names (слово перед ценой)
products = re.findall(r"([A-Za-z]+)\s+\d+\.\d{2}", text)

# 3️⃣ Extract total
total_match = re.search(r"Total:\s*(\d+\.\d{2})", text)
total = float(total_match.group(1)) if total_match else sum(prices)

# 4️⃣ Extract date
date_match = re.search(r"\d{4}-\d{2}-\d{2}", text)
date = date_match.group() if date_match else None

# 5️⃣ Extract time
time_match = re.search(r"\d{2}:\d{2}", text)
time = time_match.group() if time_match else None

# 6️⃣ Extract payment method
payment_match = re.search(r"Payment method:\s*(\w+)", text)
payment = payment_match.group(1) if payment_match else None

# Structured output
result = {
    "date": date,
    "time": time,
    "products": products,
    "prices": prices,
    "total": total,
    "payment_method": payment
}

print(json.dumps(result, indent=4))