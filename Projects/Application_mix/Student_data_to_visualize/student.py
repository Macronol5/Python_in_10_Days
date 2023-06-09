import mysql.connector
import matplotlib.pyplot as plt

class StudentPackage:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="wiley_edge_c361"
        )
        self.cursor = self.conn.cursor()

    def add_student(self, name, age,marks, subject):
        sql = "INSERT INTO students (name, age,marks, subject) VALUES (%s, %s,%s, %s)"
        values = (name, age, marks, subject)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return "Data saved Successfully"

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def get_max_marks_subject(self):
        self.cursor.execute("SELECT subject, MAX(marks) FROM students GROUP BY subject")
        return self.cursor.fetchall()

    def visualize_max_marks_subject(self):
        data = self.get_max_marks_subject()
        subjects = [record[0] for record in data]
        marks = [record[1] for record in data]

        plt.bar(subjects, marks)
        plt.xlabel('Subject')
        plt.ylabel('Marks')
        plt.title('Subject-wise Maximum Marks')

        # Save the plot as an image file
        image_path = 'static/max_marks_subject.png'
        plt.savefig(image_path)

        return image_path