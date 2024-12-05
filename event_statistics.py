from query_executor import execute_query


def event_statistics_menu(connection):
    """Handle Event Statistics Queries."""
    print("\n+-----------------------------------+")
    print("| Event Statistics Queries          |")
    print("+-----------------------------------+")
    print("1. List all events for a specific game")
    print("2. Count the number of events per game")
    print("3. Find events by type (e.g., goals, penalties)")
    print("4. Return to Main Menu")
    choice = input("Enter your choice: ")

    if choice == '1':
        game_id = input("Enter the Game ID: ")
        query = """
            SELECT play_id, event, period, periodTime 
            FROM Event 
            WHERE game_id = %s
            ORDER BY period, periodTime;
        """
        from query_executor import execute_query
        execute_query(connection, query, (game_id,))
    elif choice == '2':
        query = """
            SELECT game_id, COUNT(play_id) AS event_count
            FROM Event
            GROUP BY game_id
            ORDER BY event_count DESC;
        """
        from query_executor import execute_query
        execute_query(connection, query)
    elif choice == '3':
        event_type = input("Enter the event type (e.g., Goal, Penalty): ")
        query = """
            SELECT play_id, game_id, period, periodTime
            FROM Event
            WHERE event = %s
            ORDER BY game_id, period, periodTime;
        """
        from query_executor import execute_query
        execute_query(connection, query, (event_type,))
    elif choice == '4':
        print("Returning to Main Menu...")
    else:
        print("Invalid choice. Please try again.")

