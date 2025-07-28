import re
import menus
# from tables import setup_all_tables
# setup_all_tables()
from db import get_connection
import bcrypt

print()
print("================================")
print("Hello, welcome to Group 30's LMS")
print("================================")

def main():
    while True:
        try:
            print("Authentication:\n1. Login\n2. Sign up\n3. Exit LMS")
            choice = int(input("Enter choice (1, 2, 3): "))
            while choice not in [1, 2, 3]:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    choice = int(input("Enter choice (1, 2, 3): "))
            if choice == 1:
                login()
                break
            elif choice == 2:
                sign_up()
                break
            elif choice == 3:
                exit()
            else:                
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Password verification helper
def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def login():
    print()
    print("Welcome to our login page.")
    print("--------------------------")

    # Email pattern matching
    pattern_student = r"^[a-zA-Z0-9._%+-]+@alustudent\.com$"
    pattern_education = r"^[a-zA-Z0-9._%+-]+@alueducation\.com$"
    pattern_admin = r"^[a-zA-Z0-9._%+-]+@aluadmin\.com$"
    
    while True:
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ")

        
        connect = get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT password_hash, role FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        cursor.close()
        connect.close()

        if result:
            stored_hash, stored_role = result
            if check_password(password, stored_hash):
                #  Password matched
                print(f" Login successful. Welcome {stored_role}!")

                # Match email to expected role
                if re.match(pattern_student, email) and stored_role == "student":
                    menus.Student_menu(email)
                    break
                elif re.match(pattern_education, email) and stored_role == "instructor":
                    menus.Instructor_menu(email)
                    break
                elif re.match(pattern_admin, email) and stored_role == "admin":
                    menus.Admin_menu()
                    break
                else:
                    print(" Your email domain does not match your assigned role. Please contact admin.")
            else:
                print(" Incorrect password. Please try again.")              
        else:
            print(" No account found with that email. You may need admin approval to sign up.")
            break



def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def sign_up():
    full_name= input("Enter your full names: ")
    email= input("Enter your email: ")
    password= input("Enter your password: ")
    hashed_pw = hash_password(password)

    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""
        INSERT INTO pending_signups (full_name, email, password_hash)
        VALUES (%s, %s, %s)
    """, (full_name, email, hashed_pw))
    connect.commit()
    cursor.close()
    connect.close()

    print(" Signup request submitted. Awaiting admin approval.")


        

if __name__=='__main__':
    main()


