import mysql.connector as mysql
import os
import csv
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw_16_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(hw_16_path, 'r') as f:
    reader = csv.DictReader(f)
    for line_num, row in enumerate(reader, start=1):
        missing = []

        cursor.execute(
            "SELECT id FROM students WHERE name = %s AND second_name = %s LIMIT 1",
            (row['name'], row['second_name'])
        )
        student = cursor.fetchone()

        if not student:
            print(f"\nСтрока {line_num}:")
            print(f"  - отсутствует: студент {row['name']} {row['second_name']}")
            continue

        student_id = student['id']

        cursor.execute(
            "SELECT id FROM `groups` WHERE title = %s LIMIT 1",
            (row['group_title'],)
        )
        group = cursor.fetchone()

        if not group:
            missing.append(f"группа {row['group_title']}")
        else:
            group_id = group['id']

            cursor.execute(
                "SELECT group_id FROM students WHERE id = %s",
                (student_id,)
            )
            student_group = cursor.fetchone()

            if student_group['group_id'] != group_id:
                missing.append(f"студент не в группе {row['group_title']}")

        cursor.execute(
            "SELECT id FROM books WHERE title = %s AND taken_by_student_id = %s LIMIT 1",
            (row['book_title'], student_id)
        )
        book = cursor.fetchone()

        if not book:
            missing.append(f"книга '{row['book_title']}'")

        cursor.execute(
            "SELECT id FROM subjects WHERE title = %s LIMIT 1",
            (row['subject_title'],)
        )
        subject = cursor.fetchone()

        if not subject:
            missing.append(f"предмет '{row['subject_title']}'")
        else:
            subject_id = subject['id']

            cursor.execute(
                "SELECT id FROM lessons WHERE title = %s AND subject_id = %s LIMIT 1",
                (row['lesson_title'], subject_id)
            )
            lesson = cursor.fetchone()

            if not lesson:
                missing.append(f"занятие '{row['lesson_title']}'")
            else:
                lesson_id = lesson['id']

                cursor.execute(
                    "SELECT id FROM marks WHERE student_id = %s AND lesson_id = %s AND value = %s LIMIT 1",
                    (student_id, lesson_id, row['mark_value'])
                )
                mark = cursor.fetchone()

                if not mark:
                    missing.append(f"оценка {row['mark_value']}")

        if missing:
            print(f"\nСтрока {line_num}:")
            for item in missing:
                print(f"  - отсутствует: {item}")

db.close()
