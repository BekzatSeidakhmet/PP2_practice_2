#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#2
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#3
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
#4
words = ["hi", "hello", "ok", "python"]
for word in words:
    if len(word) < 3:
        continue
    print(word)
#5
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)