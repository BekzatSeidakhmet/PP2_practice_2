#1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#2
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
#3
numbers = [1, -2, 3, -4, 5]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1
#4
values = [0, 2, 0, 4, 6]
i = 0

while i < len(values):
    if values[i] == 0:
        i += 1
        continue
    print(values[i])
    i += 1
#5
words = ["hi", "hello", "ok", "python"]
i = 0

while i < len(words):
    if len(words[i]) < 3:
        i += 1
        continue
    print(words[i])
    i += 1