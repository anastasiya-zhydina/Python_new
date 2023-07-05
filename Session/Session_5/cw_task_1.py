# Последовательность Фибоначчи с помощью рекурсии.Найти N-ное число Фибоначчи

def fib(n):
    if n in [0]:
      return 0
    if n in [1]:
      return 1
    return fib(n-1) + fib(n-2)

list = []
num = int(input())
result = fib(num)
print(result)    