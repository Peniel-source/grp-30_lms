from .db import get_connection

def create_user_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                role ENUM('admin', 'instructor', 'student') NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def create_courses_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(100),
                description TEXT,
                instructor_id INT,
                FOREIGN KEY (instructor_id) REFERENCES users(id)
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def create_enrollments_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                course_id INT,
                enrolled_on DATE,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def create_attendance_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                course_id INT,
                status ENUM('present', 'absent', 'excused') NOT NULL,
                date DATE NOT NULL,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def create_student_status_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_status (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                course_id INT,
                status_summary TEXT,
                performance_rating ENUM('excellent', 'good', 'average', 'poor'),
                updated_on DATE,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def create_pending_signups_table():
    connect = get_connection()
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pending_signups (
                id INT PRIMARY KEY AUTO_INCREMENT,
                full_name VARCHAR(100),
                email VARCHAR(100) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                role ENUM('student', 'instructor') NOT NULL,
                requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        connect.commit()
    finally:
        cursor.close()
        connect.close()

def setup_all_tables():
    create_user_table()
    create_courses_table()
    create_enrollments_table()
    create_attendance_table()
    create_student_status_table()
    create_pending_signups_table()



    

    