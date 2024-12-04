from game_statistics import game_statistics_menu
from team_performance import team_performance_menu
from player_menu import player_performance_menu
from config_loader import connect_to_database
from main_menu import main_menu


def main():
    """Main function to handle the interface."""
    # Connect to the database
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to the database. Exiting.")
        return  # Exit if connection fails

    while True:
        # Display the main menu
        choice = main_menu()
        if choice == '1':  # Player Performance Queries
            player_performance_menu(connection)
        elif choice == '2':  # Team Performance Queries
            team_performance_menu(connection)
        elif choice == '3':  # Game Statistics Queries
            game_statistics_menu(connection)
        elif choice == '4':  # Officiating Trends Queries (Placeholder)
            print("Officiating Trends Queries are not yet implemented.")
        elif choice == '5':  # List All Teams
            query = "SELECT team_id, teamName FROM team_info ORDER BY teamName ASC;"
            from query_executor import execute_query
            execute_query(connection, query)
        elif choice == '6':  # Custom Query
            from custom_query import handle_custom_query
            handle_custom_query(connection)
        elif choice == '7':  # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    main()
