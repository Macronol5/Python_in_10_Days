from flask import Flask, render_template, request
from dataclasses import dataclass
import re

app = Flask(__name__)

#this is just to hold users data in memory
@dataclass
class User:
    name: str
    phone: str
    email: str
    country: str
    aadhar: str
    pan: str

#function which will open a file name called user_data.txt and save the data to the file.
#if the file dont exist then it will create itself and save the data.
def save_data(user):
    try:
        with open("C:/Desktop/Wiley Edge Notes/Python/user_data.txt", "a") as file:
            file.write(f"Name: {user.name}\n")
            file.write(f"Phone: {user.phone}\n")
            file.write(f"Email: {user.email}\n")
            file.write(f"Country: {user.country}\n")
            file.write(f"Aadhar: {user.aadhar}\n")
            file.write(f"PAN: {user.pan}\n")
            file.write("\n")
    except Exception as e:
        print(f"Error saving data: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    country = request.form['country']
    aadhar = request.form['aadhar']
    pan = request.form['pan']

    # The Phone Number should be 10 digits and it should contain only numbers no alphabets or special characters
    if not re.match(r'^[0-9]{10}$', phone):
        return "Invalid phone number"

    #  email it should be gmail.com and it should contain @ symbol and it should contain only alphabets, numbers, 
    # special characters like . _ % + - if not then it should return invalid email
    if not re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
        return "Invalid email"

    #  Aadhar number should be 12 digits and it should contain only numbers no alphabets or special characters.
    if not re.match(r'^[0-9]{12}$', aadhar):
        return "Invalid Aadhar number"

    #  PAN number contains 10 characters and it should be  alphabets and numbers no special characters.
    if not re.match(r'^[A-Za-z0-9]{10}$', pan):
        return "Invalid PAN number"

    user = User(name, phone, email, country, aadhar, pan)
    save_data(user)

#  If all the above conditions are satisfied then it should save the data in a file called user_data.txt and
#  return a message saying Registration successful.
    return "Registration successful"


if __name__ == '__main__':
    app.run()
