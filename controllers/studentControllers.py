from flask import render_template
from services.studentService import get_all_students, get_student

def get_students():
    students = get_all_students()
    return render_template('studentView.html', students=students)

def get_student(student_id):
    student = get_student(student_id)
    if student:
        return f"Student: {student.name}, Email: {student.email}"
    return "Student not found"

