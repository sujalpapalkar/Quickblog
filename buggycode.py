import os
import bcrypt
import sqlite3
from sqlite3 import Error

# Store secret keys securely using environment variables
SECRET_KEY = os.environ.get('SECRET_KEY')
API_KEY = os.environ.get('API_KEY')

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# Function to get a user from the database
def get_user(username):
    database = 'users.db'
    conn = create_connection(database)
    if conn is not None:
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        cur.execute(query, (username,))
        rows = cur.fetchall()
        conn.close()
        return rows
    else:
        return None

# Function to create a new user
def create_user(username, password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {
        "username": username,
        "password": hashed_password.decode('utf-8')
    }
    return user

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)

# Function to read a file
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None