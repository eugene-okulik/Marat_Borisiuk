def repeat_me(func):
    def wrapper(text, count=1):
        for i in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
