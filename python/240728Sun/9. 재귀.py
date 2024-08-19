def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num - 1)
for num in range(10):
    print(factorial(num))

def factorial2(num):
    if num > 1:
        return num* factorial2(num - 1)
    else:
        return num
for num in range(10):
    print(factorial(num))

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo (num - 2)
for num in range(10):
    print(fibo(num + 1))