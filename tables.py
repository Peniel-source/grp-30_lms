# import features.admin
# import features.instructor
# import features.student
import features.signup_approval

def Student_menu(): 
    while True:
        try:
            print("What would you like to do?:\n-------------------------")
            print("1. View Courses\n2. Check Academic Progress\n3. Check Financial Standing")
            print("4. Disciplinary Standing\n5. Request for Transcripts")
            sc= int(input("Enter your choice (1–5): "))
            while sc not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please enter a number, 1-5.")
                sc= int(input("Enter your choice (1–5): "))              
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def Instructor_menu():
    while True:
        try:
            print("What would you like to do?:\n-------------------------")
            print("1. Check Instructed Courses\n2. Create Assignments\n3. Check Attendance\n4. Check Student Records")
            ic= int(input("Enter your choice (1–4): "))
            while ic not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter a number, 1-4.")
                ic= int(input("Enter your choice (1–4): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            

def Admin_menu():
    while True:
        try:
            print("What would you like to do?:\n-------------------------")
            print("1. Manage Students\n2. Assign Instructor\n3. Issue Transcripts\n4. Generate Report\n5. View Signup Requests")
            ac= int(input("Enter your choice (1–5): "))
            while ac not in [1, 2, 3, 4, 5]:
                print("Invalid choice. Please enter a number, 1-4.")
                ac= int(input("Enter your choice (1–5): "))
            
            if ac == 5:
                features.signup_approval.admin_signup_approval_menu()
            break         
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            

