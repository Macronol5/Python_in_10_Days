from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

def connectToDatabase(user, password, host, database):
    mydb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return mydb

def fetchFromDatabase(mydb, query):
    # fetching data from the database
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult

def createApp():
    # creating a flask application
    app = Flask(__name__)
    mydb = connectToDatabase("root", "password", "localhost", "wiley_edge_c361")
    create_query = "CREATE TABLE IF NOT EXISTS test444 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"
    insert_query = "INSERT INTO test444 (name, age) VALUES (%s, %s)"
    search_query = "SELECT * FROM test444 WHERE name = %s"
    delete_query = "DELETE FROM test444 WHERE id = %s"
    mycursor = mydb.cursor()

    # this function will simply fetch data from db and display it on the homepage
    @app.route('/')
    def index():
        mycursor.execute(create_query)
        myresult = fetchFromDatabase(mydb, "SELECT * FROM test444")
        return render_template("index.html", data=myresult)

    # creating a route to insert data into the database using a form
    @app.route('/insert', methods=['GET', 'POST'])
    def insert():
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            val = (name, age)
            mycursor.execute(insert_query, val)
            mydb.commit()
            return redirect(url_for('index'))
        return render_template("insert.html")

    # creating a route to search data from the database using a form
    @app.route('/search', methods=['GET', 'POST'])
    def search():
        if request.method == 'POST':
            name = request.form['name']
            mycursor.execute(search_query, (name,))
            result = mycursor.fetchall()
            return render_template("search.html", data=result)
        return render_template("search.html")

     # deleting by taking id from url and using DELETE method
    @app.route('/delete/<id>',methods=['GET','DELETE'])
    def deleteById(id):
        mydb.deleteData(table_name,id)
        return redirect(url_for('index'))

    return app


if __name__ == "__main__":
    app = createApp()
    app.run()
