from game_statistics import game_statistics_menu
from team_performance_menu import team_performance_menu
from player_menu import player_performance_menu
from config_loader import connect_to_database
from main_menu import main_menu
from event_statistics import event_statistics_menu
from query_executor import execute_query


def season_rankings(connection):
    """Rank teams by total number of wins in the season, showing only the team names and ranks."""
    query = """
        SELECT T.teamName
        FROM team_info T
        JOIN game_teams_stats G ON T.team_id = G.team_id
        WHERE G.won = 1
        GROUP BY T.teamName
        ORDER BY COUNT(G.won) DESC;
    """
    try:
        cursor = connection.cursor(as_dict=True)
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("\nSeason Rankings (Teams Ranked by Total Wins):")
            print("+------+----------------------+")
            print("| Rank | Team Name            |")
            print("+------+----------------------+")
            # Enumerate the results to show rankings starting from 1
            for rank, result in enumerate(results, start=1):
                print(f"| {rank:<4} | {result['teamName']:<20} |")
            print("+------+----------------------+")
        else:
            print("No data found for season rankings.")
    except Exception as e:
        print(f"An error occurred while fetching season rankings: {e}")





from query_executor import execute_query

def scratches_stats_menu(connection):
    """Display the Scratches Stats submenu and execute related queries."""
    while True:
        print("+---------------------------------------+")
        print("| Scratches Stats Queries               |")
        print("+---------------------------------------+")
        print("| 1. Total Scratches by Team            |")
        print("| 2. Most Scratched Players             |")
        print("| 3. Games with the Highest Scratches   |")
        print("| 4. Scratches by Position              |")
        print("| 5. Back to Main Menu                  |")
        print("+---------------------------------------+")
        
        choice = input("Enter your choice: ")

        if choice == '5':
            print("Returning to Main Menu...")
            break

        # Queries for each menu option
        queries = [
            # 1. Total Scratches by Team
            """
            SELECT 
                ti.teamName AS team_name, 
                COUNT(gs.player_id) AS total_scratches
            FROM 
                game_scratches gs
            JOIN 
                team_info ti ON gs.team_id = ti.team_id
            GROUP BY 
                ti.teamName
            ORDER BY 
                total_scratches DESC;
            """,
            # 2. Most Scratched Players
            """
            SELECT 
                pi.firstName AS first_name, 
                pi.lastName AS last_name, 
                COUNT(gs.game_id) AS times_scratched
            FROM 
                game_scratches gs
            JOIN 
                player_info pi ON gs.player_id = pi.player_id
            GROUP BY 
                pi.player_id, pi.firstName, pi.lastName
            ORDER BY 
                times_scratched DESC
            LIMIT 10;
            """,
            # 3. Games with the Highest Scratches
            """
            SELECT 
                g.game_id, 
                g.date_time_GMT AS game_date, 
                COUNT(gs.player_id) AS total_scratches
            FROM 
                game_scratches gs
            JOIN 
                game g ON gs.game_id = g.game_id
            GROUP BY 
                g.game_id, g.date_time_GMT
            ORDER BY 
                total_scratches DESC
            LIMIT 10;
            """,
            # 4. Scratches by Position
            """
            SELECT 
                pi.primaryPosition AS position, 
                COUNT(gs.player_id) AS total_scratches
            FROM 
                game_scratches gs
            JOIN 
                player_info pi ON gs.player_id = pi.player_id
            GROUP BY 
                pi.primaryPosition
            ORDER BY 
                total_scratches DESC;
            """
        ]

        # Execute the selected query
        if choice.isdigit() and 1 <= int(choice) <= 4:
            query = queries[int(choice) - 1]
            execute_query(connection, query)
        else:
            print("Invalid choice. Please select a valid option.")









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
        elif choice == '6':  # Season Rankings
            season_rankings(connection)
        elif choice == '7':  # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
