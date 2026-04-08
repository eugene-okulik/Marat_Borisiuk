result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def number_from_result(text):
    words = text.split()
    number = int(words[-1]) + 10
    return number


print(number_from_result(result_1))
print(number_from_result(result_2))
print(number_from_result(result_3))
print(number_from_result(result_4))
