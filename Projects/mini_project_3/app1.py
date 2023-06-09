from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
def connectToDatabase(user,password,host,database):
    mydb = mysql.connector.connect(
        user="root",
        password="password",
        host="localhost",
        database="wiley_edge_c361"
    )
    return mydb
def fetchFromDatabase(mydb,query):
    # fetching data from the database
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
def createApp():
    # creating a flask application
    app = Flask(__name__)
    mydb = connectToDatabase("root","password","localhost","wiley_edge_c361")
    create_query = "CREATE TABLE IF NOT EXISTS test655 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
    insert_query = "insert into test655 (name,age) values (%s,%s)"
    search_query = "select * from test655 where name = %s"
    mycursor = mydb.cursor()
    # this function will simply fetch data from db and display it on homepage
    @app.route('/')
    def index():
        myresult = fetchFromDatabase(mydb,"SELECT * FROM test")
        return render_template("index.html", data=myresult)
    # creating a route to insert data into the database using a form
    @app.route('/insert', methods=['GET','POST'])
    def insert():
        create_query
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            val = (name,age)
            mycursor.execute(insert_query,val)
            mydb.commit()
            return redirect(url_for('index'))
        return render_template("insert.html")
    # creating a route to search data from the database using a form
    @app.route('/search',methods=['GET','POST'])
    def search():
        if request.method == 'POST':
            name = request.form['name']
            mycursor.execute(search_query,(name,))
            result = mycursor.fetchall()
            return render_template("search.html",data=result)
        return render_template("search.html")
    return app
if __name__ == "__main__":
    app = createApp()
    app.run(debug=True)
