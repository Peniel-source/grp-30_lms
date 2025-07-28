from db import get_connection
connect = get_connection()
def main():
    try:
        cursor = connect.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                Teachers_id INT PRIMARY KEY AUTO_INCREMENT,
                assignment_name VARCHAR(500) NOT NULL,
                category VARCHAR(100) NOT NULL,
                weight REAL NOT NULL CHECK (weight >= 0 AND weight <= 100),
                grade REAL NOT NULL CHECK (grade >= 0 AND grade <= 100)
            );
        """)
        
        connect.commit()

        print("\n--- Create a New Assignment ---")
    
        while True:
            assignment_name = input("Assignment Name: ").strip()
            if assignment_name:
                break
            print("Assignment name cannot be empty.")

        while True:
            category = input("Category (Formative or Summative / FA or SA): ").strip().lower()
            if category in ["formative", "fa", "summative", "sa"]:
                break
            print("Invalid category. Choose Formative, Summative, FA, or SA.")

        while True:
            try:
                weight = float(input("Weight (in %): "))
                if category in ["formative", "fa"] and 0 <= weight <= 60:
                    break
                elif category in ["summative", "sa"] and 0 <= weight <= 40:
                    break
                else:
                    print("Invalid weight for selected category.")
            except ValueError:
                print("Weight must be a number.")

        while True:
            try:
                grade = float(input("Set grade (in %): "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Grade must be a number.")

        print(f"\nAssignment '{assignment_name}' created successfully!")
        assignment_data = {            
            "assignment_name": assignment_name,
            "category": category,
            "weight": weight,
            "grade": grade
        }
        print("Assignment Data:", assignment_data)

        cursor.execute("""
            INSERT INTO assignments (assignment_name, category, weight, grade)
            VALUES (%s, %s, %s, %s)
        """, (assignment_name, category, weight, grade))
        connect.commit()
    finally:    
        cursor.close()
        connect.close()

if __name__ == "__main__":
    main()