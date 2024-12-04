from query_executor import execute_query

def team_performance_menu(connection):
    """Display the Team Performance Queries submenu."""
    while True:
        print("+---------------------------------------+")
        print("| Team Performance Queries              |")
        print("+---------------------------------------+")
        print("| 1. Teams with Most Goals              |")
        print("| 2. Teams with Best Defense            |")
        print("| 3. Teams with Most Penalty Minutes    |")
        print("| 4. Teams with Best Power Play         |")
        print("| 5. Back to Main Menu                  |")
        print("+---------------------------------------+")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Returning to Main Menu...")
            break

        queries = [
            # 1. Teams with Most Goals
            """
            SELECT 
                ti.teamName, 
                SUM(gts.goals) AS total_goals
            FROM 
                game_teams_stats gts
            JOIN 
                team_info ti ON gts.team_id = ti.team_id
            GROUP BY 
                ti.teamName
            ORDER BY 
                total_goals DESC;
            """,
            # 2. Teams with Best Defense (Fewest Goals Against)
            """
            SELECT 
                ti.teamName, 
                SUM(gts.goals) AS goals_conceded
            FROM 
                game_teams_stats gts
            JOIN 
                team_info ti ON gts.team_id = ti.team_id
            WHERE 
                gts.HoA = 'away'
            GROUP BY 
                ti.teamName
            ORDER BY 
                goals_conceded ASC;
            """,
            # 3. Teams with Most Penalty Minutes
            """
            SELECT 
                ti.teamName, 
                SUM(gts.pim) AS total_penalty_minutes
            FROM 
                game_teams_stats gts
            JOIN 
                team_info ti ON gts.team_id = ti.team_id
            GROUP BY 
                ti.teamName
            ORDER BY 
                total_penalty_minutes DESC;
            """,
            # 4. Teams with Best Power Play (Most Power Play Goals)
            """
            SELECT 
                ti.teamName, 
                SUM(gts.powerPlayGoals) AS total_power_play_goals,
                SUM(gts.powerPlayOpportunities) AS power_play_opportunities,
                (SUM(gts.powerPlayGoals) * 100.0 / SUM(gts.powerPlayOpportunities)) AS power_play_percentage
            FROM 
                game_teams_stats gts
            JOIN 
                team_info ti ON gts.team_id = ti.team_id
            GROUP BY 
                ti.teamName
            ORDER BY 
                power_play_percentage DESC;
            """
        ]

        # Validate and execute the selected query
        if choice.isdigit() and 1 <= int(choice) <= 4:
            query = queries[int(choice) - 1]
            execute_query(connection, query)
        else:
            print("Invalid choice. Please select a valid option.")
