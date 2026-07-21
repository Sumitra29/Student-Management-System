import json
import shutil
import csv
import datetime

import os
import hashlib
import random
import smtplib
import ssl
from email.message import EmailMessage
from getpass import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No users records found.")
        return []
    except json.JSONDecodeError:
        print("Error: users.json is empty or corrupted.")
        return []

def save_users(users):
    try: 
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print("users saved successfully.")
    except Exception as error:
        print(f"Error saving users: {error}")

def backup_users():
    try:
        shutil.copy("users.json", "backup_users.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("users.json file not found.")

def restore_users():
    try:
        shutil.copy("backup_users.json", "users.json")
        print("Restore Successful.")
        return load_users()
    except FileNotFoundError:
        print("Backup File Not Found.")
        return []

def register(users):

    username = input("Enter Username: ").strip()

    if username == "":
        print("Username cannot be empty.")
        return

    # Duplicate Username Check
    for user in users:
        if user["username"].lower() == username.lower():
            print("Username already exists.")
            return

    email = input("Enter Email: ").strip().lower()

    if email == "":
        print("Email cannot be empty.")
        return

    # Duplicate Email Check
    for user in users:
        if user["email"].lower() == email:
            print("Email already exists.")
            return

    password = getpass("Enter Password: ")

    if password == "":
        print("Password cannot be empty.")
        return

    confirm_password = getpass("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    print("\nSelect Role")
    print("1. Admin")
    print("2. Teacher")
    print("3. Student")

    choice = input("Enter Choice: ")

    if choice == "1":
        role = "Admin"

    elif choice == "2":
        role = "Teacher"

    elif choice == "3":
        role = "Student"

    else:
        print("Invalid Role.")
        return

    # Hash Password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user = {
        "username": username,
        "email": email,
        "password": hashed_password,
        "role": role,
        "created_at": str(datetime.date.today())
    }

    users.append(user)

    save_users(users)

    print("Registration Successful.")

logged_in_user = None

def login(users):

    global logged_in_user

    if len(users) == 0:
        print("No User Record Found.")
        return

    username = input("Enter Username: ").strip()

    password = getpass("Enter Password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for user in users:

        if (
            user["username"].lower() == username.lower()
            and user["password"] == hashed_password
        ):

            logged_in_user = user

            print("\nLogin Successful.")
            print(f"Welcome {user['username']}")
            print(f"Role : {user['role']}")

            return

    print("Invalid Username or Password.")

def logout():

    global logged_in_user

    if logged_in_user is None:
        print("No user is currently logged in.")
        return

    print(f"Goodbye, {logged_in_user['username']}")

    logged_in_user = None

    print("Logout Successful.")

def change_password(users):

    global logged_in_user

    if logged_in_user is None:
        print("Please login first.")
        return

    current_password = getpass("Enter Current Password: ")

    current_password_hash = hashlib.sha256(
        current_password.encode()
    ).hexdigest()

    if current_password_hash != logged_in_user["password"]:
        print("Current Password is incorrect.")
        return

    new_password = getpass("Enter New Password: ")

    if new_password == "":
        print("Password cannot be empty.")
        return

    if current_password == new_password:
        print("New password cannot be the same as the current password.")
        return

    confirm_password = getpass("Confirm New Password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    new_password_hash = hashlib.sha256(
        new_password.encode()
    ).hexdigest()

    # Update password
    logged_in_user["password"] = new_password_hash

    # Update users list
    for user in users:
        if user["username"] == logged_in_user["username"]:
            user["password"] = new_password_hash
            break

    save_users(users)

    print("Password Changed Successfully.")

def generate_otp():

    otp = str(random.randint(100000, 999999))
    created_at = datetime.datetime.now()

    otp_data = {
        "otp": otp,
        "created_at": str(created_at)
    }

    try:
        with open("otp.json", "w") as file:
            json.dump(otp_data, file, indent=4)
    except Exception as error:
        print(f"Error saving OTP: {error}")

    return otp, created_at

def reset_password(users):

    email = input("Enter Your Email: ").strip()

    # Check if email exists
    user = None
    for u in users:
        if u["email"] == email:
            user = u
            break

    if user is None:
        print("Email not found.")
        return

    # Load OTP
    try:
        with open("otp.json", "r") as file:
            otp_data = json.load(file)
    except FileNotFoundError:
        print("No OTP found. Please use Forgot Password first.")
        return

    entered_otp = input("Enter OTP: ")

    if entered_otp != otp_data["otp"]:
        print("Invalid OTP.")
        return

    new_password = getpass("Enter New Password: ")

    if new_password == "":
        print("Password cannot be empty.")
        return

    confirm_password = getpass("Confirm New Password: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    new_password_hash = hashlib.sha256(
        new_password.encode()
    ).hexdigest()

    user["password"] = new_password_hash

    save_users(users)

    # Delete OTP after successful reset
    if os.path.exists("otp.json"):
        os.remove("otp.json")

    print("Password Reset Successfully.")

def forgot_password(users):

    email = input("Enter Your Email: ").strip()

    # Check if email exists
    user = None

    for u in users:
        if u["email"] == email:
            user = u
            break

    if user is None:
        print("Email not found.")
        return

    # Generate OTP
    otp, created_at = generate_otp()

    # Send OTP
    if send_otp(email, otp):
        print("OTP has been sent to your registered email.")
    else:
        print("Failed to send OTP.")

def send_otp(receiver_email, otp):

    sender_email = "your_email@gmail.com"
    app_password = "your_16_character_app_password"

    subject = "Password Reset OTP"

    body = f"""
Hello,

Your OTP for password reset is: {otp}

This OTP is valid for 5 minutes.

If you did not request this, please ignore this email.

Thank you.
"""

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, app_password)

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        server.quit()

        print("OTP sent successfully.")
        return True

    except Exception as error:
        print(f"Failed to send OTP: {error}")
        return False

def export_users_csv(users):

    if len(users) == 0:
        print("No user records found.")
        return

    try:
        with open("users.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Username",
                "Email",
                "Password",
                "Role",
                "Created At"
            ])

            for user in users:
                writer.writerow([
                    user["username"],
                    user["email"],
                    user["password"],
                    user["role"],
                    user["created_at"]
                ])

        print("Users exported successfully.")

    except Exception as error:
        print(f"Error exporting users: {error}")

def import_users_csv():

    users = []

    try:
        with open("users.csv", "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                user = {
                    "username": row["Username"],
                    "email": row["Email"],
                    "password": row["Password"],
                    "role": row["Role"],
                    "created_at": row["Created At"]
                }

                users.append(user)

        save_users(users)

        print("Users imported successfully.")

        return users

    except FileNotFoundError:
        print("users.csv file not found.")
        return load_users()

    except Exception as error:
        print(f"Error importing users: {error}")
        return load_users()
                
# Menu
def authentication_menu():

    users = load_users()

    while True:

        print("\n===== Authentication Module =====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Forgot Password")
        print("6. Reset Password")
        print("7. Backup Users")
        print("8. Restore Users")
        print("9. Export Users CSV")
        print("10. Import Users CSV")
        print("11. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            register(users)

        elif choice == "2":
            login(users)

        elif choice == "3":
            logout()

        elif choice == "4":
            change_password(users)

        elif choice == "5":
            forgot_password(users)

        elif choice == "6":
            reset_password(users)

        elif choice == "7":
            backup_users()

        elif choice == "8":
            users = restore_users()

        elif choice == "9":
            export_users_csv(users)

        elif choice == "10":
            users = import_users_csv()

        elif choice == "11":
            print("Thank You")
            break

        else:
            print("Invalid Choice")