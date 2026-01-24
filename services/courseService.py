from models.courseModel import Course

def get_all_courses():
    return Course.get_all()

def get_course(course_id):
    return Course.get_by_id(course_id)

