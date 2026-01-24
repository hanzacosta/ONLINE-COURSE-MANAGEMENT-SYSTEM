from models.studentModel import Student

def get_all_students():
    return Student.get_all()

def get_student(student_id):
    return Student.get_by_id(student_id)

