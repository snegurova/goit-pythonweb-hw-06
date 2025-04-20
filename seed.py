from faker import Faker
import random
from sqlalchemy import text
from models import Student, Group, Teacher, Subject, Grade
from connect import session

fake = Faker()

def clear_data():
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.query(Group).delete()

    session.execute(text("ALTER SEQUENCE grades_id_seq RESTART WITH 1;"))
    session.execute(text("ALTER SEQUENCE students_id_seq RESTART WITH 1;"))
    session.execute(text("ALTER SEQUENCE subjects_id_seq RESTART WITH 1;"))
    session.execute(text("ALTER SEQUENCE teachers_id_seq RESTART WITH 1;"))
    session.execute(text("ALTER SEQUENCE groups_id_seq RESTART WITH 1;"))

    session.commit()

    print("All data deleted and ID sequence reset")

def seed():
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(full_name=fake.name()) for _ in range(5)]  # 5 викладачів
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=fake.job(), teacher=random.choice(teachers)) for _ in range(6)]  # 6 предметів
    session.add_all(subjects)
    session.commit()

    students = []
    for group in groups:  # Переконайся, що кожна група має хоча б одного студента
        for _ in range(random.randint(10, 15)):  # Додаємо від 10 до 15 студентів у кожну групу
            student = Student(full_name=fake.name(), group=group)
            students.append(student)
    session.add_all(students)
    session.commit()

    # Переконайся, що кожен предмет має хоча б одну оцінку
    for subject in subjects:
        student = random.choice(students)
        grade = Grade(
            student=student,
            subject=subject,
            grade=round(random.uniform(60, 100), 2),
            date_received=fake.date_between(start_date='-6m', end_date='today')
        )
        session.add(grade)

    # Додаємо оцінки для всіх студентів і предметів
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 4)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=round(random.uniform(60, 100), 2),
                    date_received=fake.date_between(start_date='-6m', end_date='today')
                )
                session.add(grade)

    session.commit()

    print("Seed completed")

if __name__ == "__main__":
    seed()
