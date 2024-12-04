from query_executor import execute_query

def game_statistics_menu(connection):
    """Display the Game Statistics Queries submenu."""
    while True:
        print("+---------------------------------------+")
        print("| Game Statistics Queries               |")
        print("+---------------------------------------+")
        print("| 1. Highest Scoring Games              |")
        print("| 2. Games with Most Penalty Minutes    |")
        print("| 3. Closest Games (Smallest Margin)    |")
        print("| 4. Longest Games by Duration          |")
        print("| 5. Back to Main Menu                  |")
        print("+---------------------------------------+")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Returning to Main Menu...")
            break

        queries = [
            # 1. Highest Scoring Games
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                (gts_away.goals + gts_home.goals) AS total_goals,
                ti_away.teamName AS away_team,
                ti_home.teamName AS home_team
            FROM 
                game g
            JOIN 
                game_teams_stats gts_away ON g.game_id = gts_away.game_id AND gts_away.HoA = 'away'
            JOIN 
                game_teams_stats gts_home ON g.game_id = gts_home.game_id AND gts_home.HoA = 'home'
            JOIN 
                team_info ti_away ON gts_away.team_id = ti_away.team_id
            JOIN 
                team_info ti_home ON gts_home.team_id = ti_home.team_id
            ORDER BY 
                total_goals DESC;
            """,
            # 2. Games with Most Penalty Minutes
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                (gts_away.pim + gts_home.pim) AS total_penalty_minutes,
                ti_away.teamName AS away_team,
                ti_home.teamName AS home_team
            FROM 
                game g
            JOIN 
                game_teams_stats gts_away ON g.game_id = gts_away.game_id AND gts_away.HoA = 'away'
            JOIN 
                game_teams_stats gts_home ON g.game_id = gts_home.game_id AND gts_home.HoA = 'home'
            JOIN 
                team_info ti_away ON gts_away.team_id = ti_away.team_id
            JOIN 
                team_info ti_home ON gts_home.team_id = ti_home.team_id
            ORDER BY 
                total_penalty_minutes DESC;
            """,
            # 3. Closest Games (Smallest Margin)
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                ABS(gts_away.goals - gts_home.goals) AS goal_margin,
                ti_away.teamName AS away_team,
                ti_home.teamName AS home_team
            FROM 
                game g
            JOIN 
                game_teams_stats gts_away ON g.game_id = gts_away.game_id AND gts_away.HoA = 'away'
            JOIN 
                game_teams_stats gts_home ON g.game_id = gts_home.game_id AND gts_home.HoA = 'home'
            JOIN 
                team_info ti_away ON gts_away.team_id = ti_away.team_id
            JOIN 
                team_info ti_home ON gts_home.team_id = ti_home.team_id
            ORDER BY 
                goal_margin ASC, g.date_time_GMT DESC;
            """,
            # 4. Longest Games by Duration
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                DATEDIFF(SECOND, g.date_time_GMT, DATEADD(MINUTE, g.duration_minutes, g.date_time_GMT)) AS game_duration_seconds,
                ti_away.teamName AS away_team,
                ti_home.teamName AS home_team
            FROM 
                game g
            JOIN 
                team_info ti_away ON g.away_team_id = ti_away.team_id
            JOIN 
                team_info ti_home ON g.home_team_id = ti_home.team_id
            ORDER BY 
                game_duration_seconds DESC;
            """
        ]

        # Validate and execute the selected query
        if choice.isdigit() and 1 <= int(choice) <= 4:
            query = queries[int(choice) - 1]
            execute_query(connection, query)
        else:
            print("Invalid choice. Please select a valid option.")
