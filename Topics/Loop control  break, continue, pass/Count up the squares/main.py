sum = 0
squares = 0
while True:
    number = int(input())
    sum += number
    squares += number ** 2
    if sum == 0:
        break
print(squares)
