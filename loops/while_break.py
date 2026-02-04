#1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#2
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
#3
numbers = [3, 7, 9, 12, 15]
i = 0

while i < len(numbers):
    if numbers[i] == 12:
        print("Found 12")
        break
    i += 1
#4
i = 1
total = 0

while True:
    total += i
    if total > 10:
        print("Total exceeded 10:", total)
        break
    i += 1
#5
while True:
    command = input("Type 'exit' to stop: ")
    if command == "exit":
        print("Program stopped")
        break
