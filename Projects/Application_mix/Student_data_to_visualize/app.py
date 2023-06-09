from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from student import *
import re
from dataclasses import dataclass

app = Flask(__name__)

conn = {
    'user' : 'root',
    'password' : 'password',
    'host' : 'localhost',
    'database' : 'wiley_edge_c361'
}

@dataclass
class Student:
    name: str
    marks : int
    subject : str

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index', methods=['GET', 'POST'])
def insert():
    name = request.form['name']
    marks = request.form['marks']
    age = request.form['age']
    subject = request.form['subject']
    
    if not re.match(r'^[a-zA-Z]$',name):
        return "Please Enter a valid name"

    if not re.match(r'^[0-9]{2}$',marks):
        return "Please Enter a valid marks"
    
    if not re.match(r'^[a-zA-Z]$',subject):
        return "Please Enter a valid subject"
    
    try: 
        conn = mysql.connector.connect(**conn)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE if not existsstudents599 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT, marks INT, subject VARCHAR(255))""")
        print ("Table created successfully")

        Student.add_student(name, age, marks, subject)
        print ("Record inserted successfully")

        print(Student.get_students())
        conn.commit()
        conn.close()
        return "Data saved Successfully"
    
    except Exception as e:
        conn.rollback()   
        return 'Error occurred while saving data to the database: ' + str(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/show_data')
def show_data():
    student_package = Student()  #package name
    max_marks_image = student_package.visualize_max_marks_subject()
    return render_template('datashow.html', max_marks_image=max_marks_image)

if __name__ == '__main__':
    app.run()