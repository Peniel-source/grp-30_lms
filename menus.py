# import features.admin
# import features.instructor
# import features.student
import signup_approval
import financial_standing
import disciplinary_status
import view_courses
import academic_progress
import create_assignments
import assign_instructor
import manage_people

from db import get_connection

def pull_assignments():
    try:
        connect = get_connection()
        cursor = connect.cursor()
        cursor.execute("SELECT assignment_name, category, weight, grade FROM assignments;")
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        connect.close()



def pull_stdnt_records():
    student_name = input("Enter the student's full name: ")
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            SELECT s.academic, s.financial, s.disciplinary
            FROM stdnt_status s
            JOIN users u ON s.user_id = u.id
            WHERE u.full_name = %s
        """, (student_name,))
        result = cursor.fetchone()
        if result:
            academic, financial, disciplinary = result
            print(f"\nCurrent status for {student_name} is:")
            print(f"Academic: {academic}")
            print(f"Financial: {financial}")
            print(f"Disciplinary: {disciplinary}")
        else:
            print("No record found for that name.")
    finally:
        cursor.close()
        connect.close()

def Student_menu(user_email): 
    while True:
        try:
            print()
            print("What would you like to do?:\n-------------------------")
            print("1. View Courses\n2. Check Academic Progress\n3. Check Financial Standing\n4. Disciplinary Standing\n5. View Assignments\n6. Exit")
            sc= int(input("Enter your choice (1–6): "))
            while sc not in [1, 2, 3, 4, 5, 6]:
                print("Invalid choice. Please enter a number, 1-6.")
                sc= int(input("Enter your choice (1–6): ")) 
            if sc == 3:
                financial_standing.pull_financial()                
            elif sc == 4:
                disciplinary_status.pull_disciplinary()                
            elif sc == 1:
                view_courses.view_courses(user_email)                
            elif sc == 2:
                academic_progress.academic_progress_checker()                
            elif sc == 5:
                for name, category, weight, grade in pull_assignments():
                    print(f"{name} | {category} | Weight: {weight}% | Grade: {grade}%")
            elif sc == 6:
                break
            else:
                print("Invalid choice")            
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def Instructor_menu(user_email):
    while True:
        try:
            print()
            print("What would you like to do?:\n-------------------------")
            print("1. See Courses Facilitate\n2. Create Assignments\n3. Check Student Records\n4. Update Academic Progress\n5. Exit")
            ic= int(input("Enter your choice (1-5): "))
            while ic not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please enter a number, 1-5.")
                ic= int(input("Enter your choice (1–5): "))
            if ic == 2:
                create_assignments.main()                
            elif ic == 1:
                view_courses.view_courses(user_email)                         
            elif ic == 4:
                academic_progress.insert_academic_status()
            elif ic == 3:
                pull_stdnt_records()
            elif ic == 5:
                break
            else:
                print("Invalid choice")            
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def Admin_menu():
    while True:
        try:
            print()
            print("What would you like to do?:\n-------------------------")
            print("1. Manage People\n2. Assign Instructor\n3. View Signup Requests\n4. Update Disciplinary\n5. Update Financial\n6. Add course\n7. Exit")
            ac= int(input("Enter your choice (1–7): "))
            while ac not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid choice. Please enter a number, 1-7.")
                ac= int(input("Enter your choice (1–7): "))            
            if ac == 3:
                signup_approval.admin_signup_approval_menu()
            elif ac == 2:
                assign_instructor.assign_inst()
            elif ac == 1:
                manage_people.manage_users()
            elif ac == 4:
                disciplinary_status.update_disciplinary_status()
            elif ac == 5:
                financial_standing.update_financial_status()
            elif ac == 6:
                assign_instructor.add_course()
            elif ac == 7:
                break
            else:
                print("Invalid input")                   
        
        except ValueError:
            print("Invalid input. Please enter a number.")