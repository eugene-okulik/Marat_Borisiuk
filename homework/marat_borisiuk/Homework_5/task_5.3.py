students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students = ', '.join(students)
subjects = ', '.join(subjects)

text = 'Students {} study these subjects: {}'
print(text.format(students, subjects))
