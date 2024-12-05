from game_statistics import game_statistics_menu
from team_performance_menu import team_performance_menu
from player_menu import player_performance_menu
from config_loader import connect_to_database
from main_menu import main_menu
from event_statistics import event_statistics_menu
from query_executor import execute_query

def season_rankings(connection):
    """Rank teams by total number of goals scored in the season, showing only the team names and ranks."""
    query = """
        SELECT T.teamName
        FROM team_info T
        JOIN game_teams_stats G ON T.team_id = G.team_id
        GROUP BY T.teamName
        ORDER BY SUM(G.goals) DESC;
    """
    results = execute_query(connection, query)
    
    if results:
        print("\nSeason Rankings (Teams Ranked by Total Goals Scored):")
        print("+----------------+-----------------+")
        print("|    Rank        |    Team Name    |")
        print("+----------------+-----------------+")
        # Enumerate the results to show rankings starting from 1
        for rank, result in enumerate(results, 1):
            # Printing the rank and the team name with formatting
            print(f"| {rank:<14} | {result['teamName']:<15} |")
        print("+----------------+-----------------+")
    else:
        print("No data found for season rankings.")

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
        elif choice == '4':  # Event Statistics Queries
            event_statistics_menu(connection)
        elif choice == '5':  # List All Teams
            query = "SELECT team_id, teamName FROM team_info ORDER BY teamName ASC;"
            execute_query(connection, query)
        elif choice == '6':  # Custom Query
            from custom_query import handle_custom_query
            handle_custom_query(connection)
        elif choice == '7':  # Season Rankings
            season_rankings(connection)
        elif choice == '8':  # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    main()
