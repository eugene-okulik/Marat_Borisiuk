import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_13_data_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(hw_13_data_path, 'r') as hw_13_data:
        for line in hw_13_data:
            yield line


now = datetime.datetime.now().date()

with open('hw_13_data2.txt', 'w') as new_file:
    for hw_13_data_line in read_file():
        parts = hw_13_data_line.split()

        if parts[0] == '1.':
            date_and_time = datetime.datetime.strptime(' '.join(parts[1:3]), '%Y-%m-%d %H:%M:%S.%f')
            new_date_and_time = date_and_time + datetime.timedelta(days=7)
            new_file.write(new_date_and_time.strftime('%Y-%m-%d %H:%M:%S.%f') + '\n')
        elif parts[0] == '2.':
            days = datetime.datetime.strptime(parts[1], '%Y-%m-%d')
            new_file.write(days.strftime('%A') + '\n')
        elif parts[0] == '3.':
            days_difference = datetime.datetime.strptime(parts[1], '%Y-%m-%d').date()
            new_file.write(f'{(now - days_difference).days}\n')
