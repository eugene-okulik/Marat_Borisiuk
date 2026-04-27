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

insert_query = "INSERT INTO subjects (title) VALUES (%s)"
values = [
    ('Алгебра112',),
    ('Геометрия112',),
    ('Физика112',)
]
cursor.executemany(insert_query, values)

cursor.execute("SELECT id FROM subjects WHERE title IN ('Алгебра112', 'Геометрия112', 'Физика112')")
subject_ids = cursor.fetchall()

insert_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = []

for subject in subject_ids:
    subject_id = subject['id']
    values.append(('lesson1_My_group_112', subject_id))
    values.append(('lesson2_My_group_112', subject_id))

cursor.executemany(insert_query, values)

cursor.execute("""
    SELECT l.id FROM lessons l
    JOIN subjects s ON l.subject_id = s.id
    WHERE s.title IN ('Алгебра112', 'Геометрия112', 'Физика112')
""")
lesson_ids = cursor.fetchall()

cursor.execute("""
    INSERT INTO marks (value, lesson_id, student_id)
    SELECT 5, l.id, %s
    FROM lessons l
    JOIN subjects s ON l.subject_id = s.id
    WHERE s.title IN ('Алгебра112', 'Геометрия112', 'Физика112')
""", (my_student_id,))
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
