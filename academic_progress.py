from db import get_connection
def academic_progress_checker():
    try:
        name = input("Enter your full name: ")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT stdnt_status.academic
                    FROM stdnt_status
                    JOIN users ON stdnt_status.user_id = users.id
                    WHERE users.full_name = %s
                """, (name,))

        result = cursor.fetchone()
    finally:
        cursor.close()
        connection.close()
    if result:
        print(f"Academic status: {result[0]}")
    else:
        print("Academic status is not available yet")


def insert_academic_status():
    name = input("What is student's full name? ")
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE full_name = %s
    """, (name,))
    student_name = cursor.fetchone()

    if student_name:
        print("Student exists")
        academic_status = input("What is student's academic status? ")

        cursor.execute("""
            SELECT id
            FROM stdnt_status
            WHERE user_id = %s
        """, (student_name[0],))
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
                UPDATE stdnt_status
                SET academic = %s
                WHERE user_id = %s
            """, (academic_status, student_name[0]))
        else:
            cursor.execute("""
                INSERT INTO stdnt_status (user_id, academic)
                VALUES (%s, %s)
            """, (student_name[0], academic_status))

        connection.commit()
        print("Academic status updated.")
    else:
        print("Student doesn't exist")
        connection.close()
    cursor.close()
    connection.close()
    return
