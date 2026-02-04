#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#3
for i in range(1, 10):
    if i == 5:
        break
    print(i)
#4
numbers = [4, 6, 9, 12, 15]
for num in numbers:
    if num == 12:
        print("Found 12")
        break
#5
total = 0
for i in range(1, 10):
    total += i
    if total > 10:
        print("Total exceeded 10:", total)
        break