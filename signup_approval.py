import re
from db import get_connection

def get_role_from_email(email):
    email = email.lower().strip()
    if re.match(r"^[a-zA-Z0-9._%+-]+@alustudent\.com$", email):
        return "student"
    elif re.match(r"^[a-zA-Z0-9._%+-]+@alueducation\.com$", email):
        return "instructor"
    elif re.match(r"^[a-zA-Z0-9._%+-]+@aluadmin\.com$", email):
        return "admin"
    else:
        return None  

def view_pending_requests():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT full_name, email, requested_at FROM pending_signups")
    requests = cursor.fetchall()
    cursor.close()
    connect.close()

    if requests:
        print("Pending Sign-Up Requests:")
        for i, req in enumerate(requests, 1):
            print(f"{i}. {req[0]} — {req[1]} — Requested on {req[2]}")
    else:
        print(" No pending requests.")

def approve_user(email):
    email = email.lower().strip()
    connect = get_connection()
    cursor = connect.cursor()

    # Check if already approved
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        print(" This email is already registered. Cannot approve again.")
        cursor.close()
        connect.close()
        return

    # Retrieve from pending_signups
    cursor.execute("SELECT full_name, email, password_hash FROM pending_signups WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        role = get_role_from_email(user[1])
        if role:
            cursor.execute("""
                INSERT INTO users (full_name, email, password_hash, role)
                VALUES (%s, %s, %s, %s)
            """, (user[0], user[1], user[2], role))

            cursor.execute("DELETE FROM pending_signups WHERE email = %s", (email,))
            connect.commit()
            print(f"{user[0]} ({role}) has been approved and added to users.")
        else:
            print(" Invalid email domain. Unable to determine role.")
    else:
        print("No pending signup found for that email.")

    cursor.close()
    connect.close()

def reject_user(email):
    email = email.lower().strip()
    connect = get_connection()
    cursor = connect.cursor()

    cursor.execute("SELECT full_name FROM pending_signups WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        cursor.execute("DELETE FROM pending_signups WHERE email = %s", (email,))
        connect.commit()
        print(f" {user[0]}'s request has been rejected and removed.")
    else:
        print(" No pending signup found for that email.")

    cursor.close()
    connect.close()

def admin_signup_approval_menu():
    while True:
        print("\n Admin Approval Menu")
        print("----------------------")
        print("1. View Pending Requests")
        print("2. Approve Signup by Email")
        print("3. Reject Signup by Email")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_pending_requests()
        elif choice == "2":
            email = input("Enter email to approve: ").strip()
            approve_user(email)
        elif choice == "3":
            email = input("Enter email to reject: ").strip()
            reject_user(email)
        elif choice == "4":
            print(" Returning to Admin Main Menu.")
            return
        else:
            print(" Invalid option. Please choose 1–4.")