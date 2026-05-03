# Bug 1: SQL injection vulnerability
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

# Bug 2: Password stored in plain text
def create_user(username, password):
    user = {
        "username": username,
        "password": password  
    }
    return user

# Bug 3: Division without zero check
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Bug 4: Hardcoded secret key
SECRET_KEY = "mysecretkey123"
API_KEY = "sk-1234567890abcdef"

# Bug 5: No error handling
def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    return content
EOF