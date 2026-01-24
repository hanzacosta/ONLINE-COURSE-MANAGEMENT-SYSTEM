from flask import Flask, render_template
from controllers import courseController, studentController

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Course routes
app.add_url_rule('/courses', view_func=courseController.get_courses)
app.add_url_rule('/courses/<int:course_id>', view_func=courseController.get_course)

# Student routes
app.add_url_rule('/students', view_func=studentController.get_students)
app.add_url_rule('/students/<int:student_id>', view_func=studentController.get_student)

if __name__ == '__main__':
    app.run(debug=True)

