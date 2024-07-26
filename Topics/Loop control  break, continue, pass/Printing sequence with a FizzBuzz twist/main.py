def print_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            break
        else:
            print(i)
        i += 1


number = int(input())
print_numbers(number)
