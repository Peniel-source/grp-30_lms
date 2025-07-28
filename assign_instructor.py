from db import get_connection


def add_course():
    while True:
        course_title = input("Enter course title or 'done' to finish: ")
        if course_title.lower() == "done":
            print("Course entry complete.")
            break

        course_description = input("Enter course description: ")
        connection = get_connection()
        cursor = connection.cursor()
        

        try:
            cursor.execute("""
                INSERT INTO courses (title, description)
                VALUES (%s, %s)
            """, (course_title, course_description))
            connection.commit()
            print(f"Course '{course_title}' added.")
        finally:
            cursor.close()
            connection.close()


def assign_inst():
    course_title = input("Enter the course title to assign an instructor to: ")
    instructor_name = input("What is the instructor's name?: ")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Find instructor
        cursor.execute("""
            SELECT id FROM users
            WHERE full_name = %s AND role = 'instructor'
        """, (instructor_name,))
        result = cursor.fetchone()

        if not result:
            print("Instructor does not exist.")
            return

        instructor_id = result[0]

        # Find course
        cursor.execute("""
            SELECT id FROM courses
            WHERE title = %s
        """, (course_title,))
        course_result = cursor.fetchone()

        if not course_result:
            print("Course not found.")
            return

        course_id = course_result[0]

        # Assign instructor
        cursor.execute("""
            UPDATE courses
            SET instructor_id = %s
            WHERE id = %s
        """, (instructor_id, course_id))
        connection.commit()
        print(f"Instructor '{instructor_name}' assigned to course '{course_title}'.")
        

    finally:
        cursor.close()
        connection.close()
# if __name__=='__main__':
#     assign_inst()
#     add_course()