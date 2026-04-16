def operation(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'

        if first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = float(input("1-е число: "))
second = float(input("2-е число: "))

result = calc(first, second)
print(f"Результат: {result}")
