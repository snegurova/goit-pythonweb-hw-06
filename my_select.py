from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from connect import engine, session

def select_1():
    return session.query(
        Student.full_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_id):
    return session.query(
        Student.full_name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Grade, Grade.student_id == Student.id) \
     .filter(Grade.subject_id == subject_id) \
     .group_by(Student.id) \
     .order_by(desc('avg_grade')) \
     .first()

def select_3(subject_id):
    return session.query(
        Group.name,
        func.avg(Grade.grade).label('avg_grade')
    ).join(Student, Student.group_id == Group.id).join(Grade, Grade.student_id == Student.id
    ).filter(Grade.subject_id == subject_id).group_by(Group.id).all()

def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.full_name).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return session.query(
        Student.full_name,
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(
        func.avg(Grade.grade)
    ).join(Grade.subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(student_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()

def select_10(student_id, teacher_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).distinct().all()

if __name__ == "__main__":  
    print("Top 5 students by average grade:")
    print(select_1())
    
    print("\nStudent with highest average grade in subject 1:")
    print(select_2(1))
    
    print("\nAverage grade per group in subject 1:")
    print(select_3(1))
    
    print("\nOverall average grade:")
    print(select_4())
    
    print("\nSubjects taught by teacher 1:")
    print(select_5(1))
    
    print("\nStudents in group 1:")
    print(select_6(1))
    
    print("\nGrades for students in group 1 for subject 1:")
    print(select_7(1, 1))
    
    print("\nAverage grade by teacher 1:")
    print(select_8(1))
    
    print("\nSubjects taken by student 1:")
    print(select_9(1))
    
    print("\nCourses taught by teacher 1 to student 1:")
    print(select_10(1, 1))
