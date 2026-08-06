import sqlite3
import hashlib
import hmac
import subprocess

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

PASSWORD_SALT = b"mysalt123"
PBKDF2_ITERATIONS = 100000

ADMIN_USERNAME = "admin"

ADMIN_PASSWORD_HASH = hashlib.pbkdf2_hmac(
    "sha256",
    b"admin123",
    PASSWORD_SALT,
    PBKDF2_ITERATIONS
)


def login():
    username = input("Username: ")
    password = input("Password: ")

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        PASSWORD_SALT,
        PBKDF2_ITERATIONS
    )

    if username == ADMIN_USERNAME and hmac.compare_digest(password_hash, ADMIN_PASSWORD_HASH):
        print("Login Successful")
    else:
        print("Invalid Login")


def search_student():
    roll = input("Enter Roll Number: ")

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (roll,)
    )

    result = cursor.fetchall()

    if result:
        for row in result:
            print(row)
    else:
        print("Student not found")


def list_files():
    subprocess.run(["ls"])


def menu():
    while True:

        print("\n------ Student System ------")
        print("1. Login")
        print("2. Search Student")
        print("3. List Files")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            login()

        elif choice == "2":
            search_student()

        elif choice == "3":
            list_files()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


menu()

conn.close()
