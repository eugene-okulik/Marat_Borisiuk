import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)",
               ('John', 'Jim2', None))
my_student_id = cursor.lastrowid

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Первая книга', my_student_id),
    ('Вторая книга', my_student_id),
    ('Третья книга', my_student_id)
]
cursor.executemany(insert_query, values)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('My group 112', 'apr 2026', 'june 2026'))
my_group_id = cursor.lastrowid

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s", (my_group_id, my_student_id))

subject_ids = []
subjects = ['Алгебра112', 'Геометрия112', 'Физика112']

for title in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subject_ids.append(cursor.lastrowid)

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_ids = []

for subject_id in subject_ids:
    cursor.execute(insert_query, ('lesson1_My_group_112', subject_id))
    lesson_ids.append(cursor.lastrowid)

    cursor.execute(insert_query, ('lesson2_My_group_112', subject_id))
    lesson_ids.append(cursor.lastrowid)

insert_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = []

stud_marks = [5, 4, 5, 4, 5, 4]

for i, lesson_id in enumerate(lesson_ids):
    values.append((stud_marks[i], lesson_id, my_student_id))

cursor.executemany(insert_query, values)
db.commit()

cursor.execute("SELECT value FROM marks WHERE student_id = %s", (my_student_id,))
marks = cursor.fetchall()
for mark in marks:
    print(mark['value'])

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s", (my_student_id,))
books = cursor.fetchall()
for book in books:
    print(book['title'])

query = """
    SELECT * FROM students s
    JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
"""
cursor.execute(query, (my_student_id,))
results = cursor.fetchall()

for info in results:
    print(info)

db.close()
