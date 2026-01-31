Python
from repositories.courseRepository import CourseRepository
# Assume a similar StudentRepository exists
from repositories.studentRepository import StudentRepository 

class RepositoryFactory:
    @staticmethod
    def get_repository(repo_type):
        if repo_type == 'course':
            return CourseRepository()
        elif repo_type == 'student':
            return StudentRepository()
        return None
