from query_executor import execute_query
from prettytable import PrettyTable

def event_statistics_menu(connection):
    """Handle Event Statistics Queries."""
    while True:
        print("\n+-----------------------------------+")
        print("| Event Statistics Queries          |")
        print("+-----------------------------------+")
        print("1. List all events for a specific game")
        print("2. Count the number of events per game")
        print("3. Find events by type (e.g., goals, penalties)")
        print("4. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':  # List all events for a specific game
            game_id = input("Enter the Game ID: ")
            query = """
                SELECT play_id, event, period, periodTime 
                FROM Event 
                WHERE game_id = %s
                ORDER BY period, periodTime;
            """
            try:
                cursor = connection.cursor(as_dict=True)
                cursor.execute(query, (game_id,))
                results = cursor.fetchall()

                if not results:
                    print(f"No events found for game ID: {game_id}.")
                    continue

                # Display events in a table
                table = PrettyTable()
                table.field_names = ["play_id", "event", "period", "periodTime"]
                for row in results:
                    table.add_row([row["play_id"], row["event"], row["period"], row["periodTime"]])
                print(table)

            except Exception as e:
                print(f"Failed to execute query. Error: {e}")

        elif choice == '2':  # Count the number of events per game
            query = """
                SELECT game_id, COUNT(play_id) AS event_count
                FROM Event
                GROUP BY game_id
                ORDER BY event_count DESC;
            """
            try:
                cursor = connection.cursor(as_dict=True)
                cursor.execute(query)
                results = cursor.fetchall()

                if not results:
                    print("No events found.")
                    continue

                # Display event counts in a table
                table = PrettyTable()
                table.field_names = ["game_id", "event_count"]
                for row in results:
                    table.add_row([row["game_id"], row["event_count"]])
                print(table)

            except Exception as e:
                print(f"Failed to execute query. Error: {e}")

        elif choice == '3':  # Find events by type (e.g., goals, penalties)
            event_type = input("Enter the event type (e.g., Goal, Penalty): ")
            query = """
                SELECT play_id, game_id, period, periodTime
                FROM Event
                WHERE event = %s
                ORDER BY game_id, period, periodTime;
            """
            try:
                cursor = connection.cursor(as_dict=True)
                cursor.execute(query, (event_type,))
                results = cursor.fetchall()

                if not results:
                    print(f"No events of type '{event_type}' found.")
                    continue

                # Display events of the specified type in a table
                table = PrettyTable()
                table.field_names = ["play_id", "game_id", "period", "periodTime"]
                for row in results:
                    table.add_row([row["play_id"], row["game_id"], row["period"], row["periodTime"]])
                print(table)

            except Exception as e:
                print(f"Failed to execute query. Error: {e}")

        elif choice == '4':  # Return to Main Menu
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")
