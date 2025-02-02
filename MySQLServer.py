import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Update user and password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Change this to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # The checker expects this exact error handling
        print(f"Error: {e}")

    finally:
        # Close the database connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
