n = int(input())
fib = [0, 1]
if n >= 2:
    for i in range(n):
        x = fib[-1] + fib[-2]
        fib.append(x)
print(fib)
