from config.database import get_connection

class Course:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = [Course(row['id'], row['name'], row['description']) for row in cursor.fetchall()]
        conn.close()
        return courses

    @staticmethod
    def get_by_id(course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE id=?", (course_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Course(row['id'], row['name'], row['description'])
        return None

