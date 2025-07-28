def manage_users():
    from db import get_connection
    while True:
        try:
            connect = get_connection()
            cursor = connect.cursor()

            print("\n====MANAGE LMS USERS====")
            print("\n1. See all users\n2. Remove People\n3. Exit")
            choice = int(input("Enter your choice (1-3): "))

            while choice not in [1, 2, 3]:
                print("Invalid choice. Enter 1, 2, or 3.")
                choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                cursor.execute("SELECT full_name, email, role FROM users;")
                users = cursor.fetchall()
                print("\n--- List of Users ---")
                for i in users:
                    full_name, email, role = i
                    print(f"Name: {full_name} -- Email: {email} -- Role: {role}s")              
            elif choice == 2:
                cursor.execute("SELECT full_name FROM users;")
                users = [row[0] for row in cursor.fetchall()]                
                person = input("Enter the full name of the user you want to remove: ").strip()
                cursor.execute("SELECT id FROM users WHERE full_name = %s", (person,))
                result = cursor.fetchone()
                if not result:
                    print("User not found")
                    return
                user_id = result[0]
                cursor.execute("""
                    UPDATE courses
                    SET instructor_id = NULL
                    WHERE instructor_id = %s
                """, (user_id,))
                
                if person in users:
                    cursor.execute("DELETE FROM users WHERE full_name = %s;", (person,))
                    connect.commit()
                    print(f"'{person}' has been removed.")
                else:
                    print("Person not found")                 
            elif choice == 3:
                print("Returning to admin menu")
                return
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter a number, either 1, 2 or 3.")

        finally:
            cursor.close()
            connect.close()

if __name__ == "__main__":
    manage_users()



    
