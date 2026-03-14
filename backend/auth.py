from database import cursor, db
import random

def signup():

    email = input("Enter email: ")
    password = input("Enter password: ")

    cursor.execute(
        "INSERT INTO users(email,password) VALUES(%s,%s)",
        (email,password)
    )

    db.commit()
    print("Account created")

def login():

    email = input("Email: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    for u in users:

        if u["email"] == email:

            if u["password"] == password:

                print("Login successful")
                return True

            else:
                print("Wrong password")
                return False

    print("User not found")
    return False

def forgot_password():

    email = input("Enter email: ")

    otp = random.randint(1000,9999)

    print("OTP:",otp)

    entered = int(input("Enter OTP: "))

    if entered == otp:

        new_pass = input("New password: ")

        cursor.execute(
        "UPDATE users SET password=%s WHERE email=%s",
        (new_pass,email)
        )

        db.commit()

        print("Password updated")

    else:
        print("Invalid OTP")