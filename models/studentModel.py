from config.database import get_connection

class Student:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = [Student(row['id'], row['name'], row['email']) for row in cursor.fetchall()]
        conn.close()
        return students

    @staticmethod
    def get_by_id(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Student(row['id'], row['name'], row['email'])
        return None

