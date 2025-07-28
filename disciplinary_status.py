from db import get_connection
connect = get_connection()
try:
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stdnt_status (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        financial VARCHAR(3000),
        disciplinary VARCHAR(3000),
        academic ENUM('excellent', 'good', 'average', 'poor'),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """)
    connect.commit()
finally:
    cursor.close()
    connect.close()

def status():
    student_name = input("What is the student's name? ")
    
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM users WHERE full_name = %s", (student_name,))
    results = cursor.fetchone()
    cursor.close()
    connect.close()
    
    if results:
        print("Student exists.")
        user_id = results[0]
        dis_status = input("What is their disciplinary status? ")
        return user_id, dis_status
    else:
        print("Student doesn't exist.")
        return None, None

def update_disciplinary_status():
    user_id, dis_status = status()

    if dis_status is not None and user_id is not None:
        connect = get_connection()   

        try:
            cursor = connect.cursor()
            cursor.execute("SELECT id FROM stdnt_status WHERE user_id = %s", (user_id,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    "UPDATE stdnt_status SET disciplinary = %s WHERE user_id = %s",
                    (dis_status, user_id)
                )
            else:
                cursor.execute(
                    "INSERT INTO stdnt_status (user_id, disciplinary) VALUES (%s, %s)",
                    (user_id, dis_status)
                )

            connect.commit()
            print("Disciplinary status updated.")
        finally:
            cursor.close()
            connect.close()
    else:
        print("Cannot update disciplinary standing.")
    return

def pull_disciplinary():
    student_name = input("Enter your full name: ")

    connect = get_connection()
    try:
        cursor = connect.cursor()  
        cursor.execute("""
            SELECT s.disciplinary
            FROM stdnt_status s
            JOIN users u ON s.user_id = u.id
            WHERE u.full_name = %s
        """, (student_name,))
        result = cursor.fetchone()
    finally:
        cursor.close()
        connect.close()

    if result and result[0]:
        print(f"Disciplinary status for {student_name}: {result[0]}")
    else:
        print("No disciplinary status or student not found.")


