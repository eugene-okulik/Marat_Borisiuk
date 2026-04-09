def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
positions = [5, 200, 1000, 100000]
current = 0

for pos in positions:
    while current < pos:
        number = next(fib)
        current += 1
    print(number)
