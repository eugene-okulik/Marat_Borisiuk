INSERT INTO students (name, second_name, group_id) VALUES ('John', 'Jin', 1);

INSERT INTO books (title, taken_by_student_id)
VALUES ('Первая', 22850), ('Вторая', 22850), ('Синяя', 22850);

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('My group №111', 'apr 2026', 'june 2026');

UPDATE students
SET group_id = (SELECT id FROM `groups` WHERE title = 'My group №111' AND start_date = 'apr 2026')
WHERE id = 22850;


INSERT INTO subjects (title) VALUES ('Алгебра111'), ('Геометрия111'), ('Физика111');

INSERT INTO lessons (title, subject_id)
VALUES ('lesson1_My_group_№111', (SELECT id FROM subjects WHERE title = 'Алгебра111')),
	   ('lesson2_My_group_№111', (SELECT id FROM subjects WHERE title = 'Алгебра111')),
       ('lesson1_My_group_№111', (SELECT id FROM subjects WHERE title = 'Геометрия111')),
       ('lesson2_My_group_№111', (SELECT id FROM subjects WHERE title = 'Геометрия111')),
       ('lesson1_My_group_№111', (SELECT id FROM subjects WHERE title = 'Физика111')),
       ('lesson2_My_group_№111', (SELECT id FROM subjects WHERE title = 'Физика111'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES (2, (SELECT id FROM lessons WHERE title = 'lesson1_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Алгебра111')), 22850),
       (4, (SELECT id FROM lessons WHERE title = 'lesson2_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Алгебра111')), 22850),
       (5, (SELECT id FROM lessons WHERE title = 'lesson1_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Геометрия111')), 22850),
       (5, (SELECT id FROM lessons WHERE title = 'lesson2_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Геометрия111')), 22850),
       (5, (SELECT id FROM lessons WHERE title = 'lesson1_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Физика111')), 22850),
       (5, (SELECT id FROM lessons WHERE title = 'lesson2_My_group_№111' AND subject_id = (SELECT id FROM subjects WHERE title = 'Физика111')), 22850);

SELECT value FROM marks WHERE student_id = 22850

SELECT title FROM books WHERE taken_by_student_id = 22850

SELECT * FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects sub ON l.subject_id= sub.id
WHERE s.id = 22850