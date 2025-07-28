from db import get_connection


def view_courses(user_email):
    # user_email = input("Enter your email: ").strip()      
    connect = get_connection()
    cursor = connect.cursor()    
    cursor.execute("SELECT role FROM users WHERE email = %s", (user_email,))
    result = cursor.fetchone()
      
    if result:
        role = result[0]  
    else:
        print("No user found with that email.")
        return


    if role == 'student':
        print(f"\nCourses enrolled by {user_email}:")
        cursor.execute("""
            SELECT title, description FROM courses""")        
        courses = cursor.fetchall()

    elif role == 'instructor':
        print(f"\nCourses facilitated by {user_email}:")
        cursor.execute("""
            SELECT *
            FROM courses
        """)
        courses = cursor.fetchall()

    elif role == 'admin':
        print("\nAll Available Courses:")
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()  
    else:
        print("Unknown role.")
        cursor.close()
        connect.close()
        return

    if courses:
        print("\nCourses:")
        for course in courses:
            print(f"- {course[1]} (Course ID: {course[0]})")
    else:
        print("No courses found.")

    cursor.close()
    connect.close()

if __name__=='__main__':
    view_courses()