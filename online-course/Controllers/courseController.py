from flask import render_template
from services.courseService import get_all_courses, get_course

def get_courses():
    courses = get_all_courses()
    return render_template('courseView.html', courses=courses)

def get_course(course_id):
    course = get_course(course_id)
    if course:
        return f"Course: {course.name}, Description: {course.description}"
    return "Course not found"

