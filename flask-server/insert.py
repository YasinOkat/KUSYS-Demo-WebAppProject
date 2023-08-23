import psycopg2
import bcrypt

# Replace these values with your actual database connection details
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "1234"

users = [
    ("yasin", "123456", "admin"),
]

try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    insert_query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"

    # Hash passwords and insert each user into the database
    for username, password, role in users:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute(insert_query, (username, hashed_password, role))

    # Commit the changes and close the cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

    print("Users inserted successfully!")

except psycopg2.Error as error:
    print("Error inserting users:", error)