def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully!")
    except Exception as e:
        print(f"Error executing query: {e}")

def fetch_data(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
