import argparse
from connect import session
from models import Teacher, Group, Student, Subject, Grade


def create_teacher(args):
    teacher = Teacher(full_name=args.name)
    session.add(teacher)
    session.commit()
    print(f"Created Teacher: {teacher.full_name}")

def list_teachers(_):
    teachers = session.query(Teacher).all()
    for t in teachers:
        print(f"{t.id}: {t.full_name}")

def update_teacher(args):
    teacher = session.query(Teacher).filter_by(id=args.id).first()
    if teacher:
        teacher.full_name = args.name
        session.commit()
        print(f"Updated Teacher ID {args.id} to {teacher.full_name}")
    else:
        print(f"Teacher with ID {args.id} not found")

def remove_teacher(args):
    teacher = session.query(Teacher).filter_by(id=args.id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Removed Teacher ID {args.id}")
    else:
        print(f"Teacher with ID {args.id} not found")


def create_group(args):
    group = Group(name=args.name)
    session.add(group)
    session.commit()
    print(f"Created Group: {group.name}")

def list_groups(_):
    groups = session.query(Group).all()
    for g in groups:
        print(f"{g.id}: {g.name}")

def update_group(args):
    group = session.query(Group).filter_by(id=args.id).first()
    if group:
        group.name = args.name
        session.commit()
        print(f"Updated Group ID {args.id} to {group.name}")
    else:
        print(f"Group with ID {args.id} not found")

def remove_group(args):
    group = session.query(Group).filter_by(id=args.id).first()
    if group:
        session.delete(group)
        session.commit()
        print(f"Removed Group ID {args.id}")
    else:
        print(f"Group with ID {args.id} not found")
def create_student(args):
    student = Student(full_name=args.name, group_id=args.group_id)
    session.add(student)
    session.commit()
    print(f"Created Student: {student.full_name} (Group ID: {student.group_id})")

def list_students(_):
    students = session.query(Student).all()
    for s in students:
        print(f"{s.id}: {s.full_name} (Group ID: {s.group_id})")

def update_student(args):
    student = session.query(Student).filter_by(id=args.id).first()
    if student:
        if args.name:
            student.full_name = args.name
        if args.group_id:
            student.group_id = args.group_id
        session.commit()
        print(f"Updated Student ID {args.id}")
    else:
        print(f"Student with ID {args.id} not found")

def remove_student(args):
    student = session.query(Student).filter_by(id=args.id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Removed Student ID {args.id}")
    else:
        print(f"Student with ID {args.id} not found")

def create_grade(args):
    grade = Grade(
        student_id=args.student_id,
        subject_id=args.subject_id,
        grade=args.grade,
        date_received=args.date_received
    )
    session.add(grade)
    session.commit()
    print(f"Created Grade: {grade.grade} (Student ID: {grade.student_id}, Subject ID: {grade.subject_id})")

def list_grades(_):
    grades = session.query(Grade).all()
    for g in grades:
        print(f"{g.id}: {g.grade} (Student ID: {g.student_id}, Subject ID: {g.subject_id}, Date: {g.date_received})")

def update_grade(args):
    grade = session.query(Grade).filter_by(id=args.id).first()
    if grade:
        if args.grade is not None:
            grade.grade = args.grade
        if args.student_id:
            grade.student_id = args.student_id
        if args.subject_id:
            grade.subject_id = args.subject_id
        if args.date_received:
            grade.date_received = args.date_received
        session.commit()
        print(f"Updated Grade ID {args.id}")
    else:
        print(f"Grade with ID {args.id} not found")

def remove_grade(args):
    grade = session.query(Grade).filter_by(id=args.id).first()
    if grade:
        session.delete(grade)
        session.commit()
        print(f"Removed Grade ID {args.id}")
    else:
        print(f"Grade with ID {args.id} not found")

def create_subject(args):
    subject = Subject(name=args.name, teacher_id=args.teacher_id)
    session.add(subject)
    session.commit()
    print(f"Created Subject: {subject.name} (Teacher ID: {subject.teacher_id})")

def list_subjects(_):
    subjects = session.query(Subject).all()
    for s in subjects:
        print(f"{s.id}: {s.name} (Teacher ID: {s.teacher_id})")

def update_subject(args):
    subject = session.query(Subject).filter_by(id=args.id).first()
    if subject:
        if args.name:
            subject.name = args.name
        if args.teacher_id:
            subject.teacher_id = args.teacher_id
        session.commit()
        print(f"Updated Subject ID {args.id}")
    else:
        print(f"Subject with ID {args.id} not found")

def remove_subject(args):
    subject = session.query(Subject).filter_by(id=args.id).first()
    if subject:
        session.delete(subject)
        session.commit()
        print(f"Removed Subject ID {args.id}")
    else:
        print(f"Subject with ID {args.id} not found")

ACTION_FUNCTIONS = {
    'Teacher': {
        'create': create_teacher,
        'list': list_teachers,
        'update': update_teacher,
        'remove': remove_teacher
    },
    'Group': {
        'create': create_group,
        'list': list_groups,
        'update': update_group,
        'remove': remove_group
    },
    'Student': {
        'create': create_student,
        'list': list_students,
        'update': update_student,
        'remove': remove_student
    },
    'Grade': {
        'create': create_grade,
        'list': list_grades,
        'update': update_grade,
        'remove': remove_grade
    },
    'Subject': {
        'create': create_subject,
        'list': list_subjects,
        'update': update_subject,
        'remove': remove_subject
    },
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'remove'], required=True)
    parser.add_argument('-m', '--model', choices=ACTION_FUNCTIONS.keys(), required=True)
    parser.add_argument('--id', type=int, help='ID запису для оновлення або видалення')
    parser.add_argument('-n', '--name', help='Ім’я (для створення або оновлення)')
    parser.add_argument('-gid', '--group-id', type=int, help='ID групи для студента')
    parser.add_argument('-sid', '--student-id', type=int, help='ID студента для оцінки')
    parser.add_argument('-sbid', '--subject-id', type=int, help='ID предмета для оцінки')
    parser.add_argument('--grade', type=float, help='Оцінка')
    parser.add_argument('--date-received', type=str, help='Дата отримання оцінки (YYYY-MM-DD)')
    parser.add_argument('-tid', '--teacher-id', type=int, help='ID викладача для предмета')

    args = parser.parse_args()
    action_map = ACTION_FUNCTIONS.get(args.model)

    if not action_map:
        print(f"Unknown model {args.model}")
        return

    action_func = action_map.get(args.action)
    if not action_func:
        print(f"Action {args.action} not supported for model {args.model}")
        return

    action_func(args)


if __name__ == '__main__':
    main()
