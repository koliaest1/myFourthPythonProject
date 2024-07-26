count = 0
summ = 0
while True:
    value = input()
    if value == ".":
        break
    else:
        summ += int(value)
        count += 1
print(summ / count)
