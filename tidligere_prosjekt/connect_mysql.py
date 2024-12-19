import mysql.connector
from mysql.connector import Error

def connect_to_database(host, user, password, database):
    """
    Connect to a MySQL database and return the connection object.

    Parameters:
        host (str): Hostname or IP address of the MySQL server.
        user (str): Username to authenticate with the MySQL server.
        password (str): Password for the MySQL user.
        database (str): Name of the database to connect to.

    Returns:
        connection: MySQL connection object if successful, None otherwise.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

    return None

def main():
    # Replace the following with your database connection details
    host = "localhost"  # or the IP address of your MySQL server
    user = "root"        # your MySQL username
    password = "yourpassword"  # your MySQL password
    database = "yourdatabase"  # your database name

    # Connect to the database
    connection = connect_to_database(host, user, password, database)

    if connection:
        try:
            # Example query
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Connected to database: {record}")

        finally:
            # Close the connection
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
