def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


ans = factorial(8)
print(ans)
