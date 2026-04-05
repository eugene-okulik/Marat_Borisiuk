# esult = 'результат операции: 42'
# result = 'результат операции: 514'
result = 'результат работы программы: 9'

colon_index = result.index(':')
number_start = colon_index + 2
number = int(result[number_start:])

print(number + 10)