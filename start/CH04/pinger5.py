def is_divisible(number, divisor):
    return number % divisor == 0

number = int(input("Enter a number: "))
divisor = int(input("Enter a divisor: "))

if is_divisible(number, divisor):
    print(f"{number} is divisible by {divisor}.")
else:
    print(f"{number} is not divisible by {divisor}.")
