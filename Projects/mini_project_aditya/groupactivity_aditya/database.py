import mysql.connector
import re
class Database:
    def __init__(self,user,password,host,database,table_name):
        self.connect(user,password,host,database)
        self.createTable(table_name)
        
    
    def connect(self,user,password,host,database):
        self.db = mysql.connector.connect(
            user = user,
            password = password,
            host = host,
            database = database
        )
    
    def createTable(self,table_name):
        cursor = self.db.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

    def insertData(self,table_name, name,age):
        cursor = self.db.cursor()
        insert_query = f"INSERT INTO {table_name} (name,age) VALUES (%s,%s)"
        # check name, age using regex

        if not name or not age:
            return "Name or age is empty"
        
        if not re.match("^[a-zA-Z ]*$",name):
            return "Name is not valid"
        
        if not re.match("^[0-9]*$",age):
            return "Age is not valid"
        
        val = (name,age)
        cursor.execute(insert_query,val)
        self.db.commit()

        return "Data inserted successfully"

    def searchData(self,table_name,name):
        cursor = self.db.cursor()

        if not re.match("^[a-zA-Z ]*$",name):
            return []

        search_query = f"SELECT * FROM {table_name} WHERE name = %s"
        cursor.execute(search_query,(name,))
        result = cursor.fetchall()
        return result
    
    # function to delete by id
    def deleteData(self,table_name,id):
        cursor = self.db.cursor()
        delete_query = f"DELETE FROM {table_name} WHERE id = %s"
        cursor.execute(delete_query,(id,))
        self.db.commit()
        return "Data deleted successfully"

    def fetchAllData(self,table_name):
        cursor = self.db.cursor()
        fetch_query = f"SELECT * FROM {table_name}"
        cursor.execute(fetch_query)
        result = cursor.fetchall()
        return result
    
    # exporting this class to be used in other files