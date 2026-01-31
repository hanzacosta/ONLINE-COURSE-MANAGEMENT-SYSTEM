Python
from config.database import DatabaseConnection
from models.courseModel import Course

class CourseRepository:
    def __init__(self):
        self.db = DatabaseConnection().get_connection()

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM courses")
        return [Course(row['id'], row['name'], row['description']) for row in cursor.fetchall()]

    def get_by_id(self, course_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM courses WHERE id=?", (course_id,))
        row = cursor.fetchone()
        return Course(row['id'], row['name'], row['description']) if row else None

