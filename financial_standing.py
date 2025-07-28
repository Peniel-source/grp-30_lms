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
        fin_status = input("What is their financial status? ")
        return user_id, fin_status
    else:
        print("Student doesn't exist.")
        return None, None

def update_financial_status():   
    user_id, fin_status = status()
    if fin_status is not None and user_id is not None:
        connect = get_connection()        
        try:
            cursor = connect.cursor()
            cursor.execute("SELECT id FROM stdnt_status WHERE user_id = %s", (user_id,))
            existing = cursor.fetchone()

            if existing:
                cursor.execute(
                    "UPDATE stdnt_status SET financial = %s WHERE user_id = %s",
                    (fin_status, user_id)
                )
            else:
                cursor.execute(
                    "INSERT INTO stdnt_status (user_id, financial) VALUES (%s, %s)",
                    (user_id, fin_status)
                )

            connect.commit()
            print("Financial status updated.")
        finally:
            cursor.close()
            connect.close()
    else:
        print("Cannot update financial standing.")
    return

def pull_financial():
    student_name = input("Enter your full name: ")
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            SELECT s.financial
            FROM stdnt_status s
            JOIN users u ON s.user_id = u.id
            WHERE u.full_name = %s
        """, (student_name,))
        result = cursor.fetchone()
    finally:
        cursor.close()
        connect.close()
    if result:
        print(f"Financial status for {student_name}: {result[0]}")
    else:
        print("Student not found or no financial status.")

