from config_loader import connect_to_database
from main_menu import main_menu
from player_menu import player_performance_menu
from custom_query import handle_custom_query
from query_executor import execute_query

def list_all_teams(connection):
    """List all teams in the database."""
    query = "SELECT team_id, teamName FROM team_info;"
    try:
        cursor = connection.cursor(as_dict=True)
        cursor.execute(query)
        results = cursor.fetchall()
        print("+----------------+----------------+")
        print("| Team ID        | Team Name      |")
        print("+----------------+----------------+")
        for row in results:
            print(f"| {row['team_id']:<14} | {row['teamName']:<14} |")
        print("+----------------+----------------+")
    except Exception as e:
        print("Failed to execute query. Error:", e)

def main():
    """Main function to handle the interface."""
    connection = connect_to_database()
    if not connection:
        return

    while True:
        choice = main_menu()
        if choice == '1':
            player_performance_menu()
        elif choice == '5':
            list_all_teams(connection)
        elif choice == '6':
            handle_custom_query(connection)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Feature not implemented yet. Stay tuned!")

    connection.close()

if __name__ == "__main__":
    main()

