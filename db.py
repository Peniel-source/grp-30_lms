import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql-group30lms-alustudent-201e.f.aivencloud.com",
        user="avnadmin",
        password="AVNS_zgAZVArImEYHstZ1red",  # Paste your password here
        database="defaultdb",
        port=25302,
        ssl_ca=r"C:\Users\HP\Downloads\ca.pem"  # Use raw string or forward slashes to avoid unicodeescape error
    )


# cursor = conn.cursor()
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()

# if tables:
#     print("Tables in database:")
#     for (table,) in tables:
#         print(f"- {table}")
# else:
#     print("✅ Connected successfully — but no tables found yet.")














