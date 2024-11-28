import pyodbc
import configparser

def load_config():
    """Load database credentials from auth.config."""
    config = configparser.ConfigParser()
    config.read("auth.config")
    return config["database"]

def connect_to_database():
    """Establish a connection to the database using credentials from auth.config."""
    config = load_config()
    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={config["server"]};'
            f'DATABASE={config["database"]};'
            f'UID={config["username"]};'
            f'PWD={config["password"]}'
        )
        print("Connected to the database successfully!")
        return connection
    except Exception as e:
        print("Failed to connect to the database. Error:", e)
        return None

def main_menu():
    print("+---------------------------------------+")
    print("| NHL Query Interface                   |")
    print("+---------------------------------------+")
    print("| 1. Player Performance Queries         |")
    print("| 2. Team Dynamics Queries              |")
    print("| 3. Game Statistics Queries            |")
    print("| 4. Officiating Trends Queries         |")
    print("| 5. Custom Query                       |")
    print("| 6. Help                               |")
    print("| 7. Exit                               |")
    print("+---------------------------------------+")
    choice = input("Enter your choice: ")
    return choice

def execute_query(connection, query, parameters=None):
    """Execute a SQL query and print the results."""
    try:
        cursor = connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Failed to execute query. Error:", e)

def handle_custom_query(connection):
    """Allow the user to run a custom query."""
    print("Enter your custom SQL query (type 'exit' to return to the main menu):")
    while True:
        query = input("SQL> ")
        if query.lower() == 'exit':
            break
        execute_query(connection, query)

def main():
    """Main function to handle the interface."""
    connection = connect_to_database()
    if not connection:
        return

    while True:
        choice = main_menu()
        if choice == '5':
            handle_custom_query(connection)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Feature not implemented yet. Stay tuned!")

    connection.close()

if __name__ == "__main__":
    main()

