from flask import Flask
import mysql.connector  

app = Flask(__name__)

@app.route('/')
def retrieve_data():
    try:
        conn = mysql.connector.connect(
            host  = "localhost",
            user = "root",
            password = "password",
            database = "wiley_edge_c361"
        )

        cursor = conn.cursor()
        cursor.execute("select * from users789")

        rows = cursor.fetchall()

        data = ''

        for row in rows:
            name, phone, email, country, aadhar, pan = row
        data += f"Name: {name}, Phone: {phone}, Email: {email}, Country: {country}, Aadhar: {aadhar}, PAN: {pan}<br>"
        

        conn.commit()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        return "Error in mysql connection"


if __name__ == '__main__':
    app.run() 
