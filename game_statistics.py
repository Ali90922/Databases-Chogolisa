from query_executor import execute_query


def game_statistics_menu(connection):
    """Display the Game Statistics Queries submenu."""
    while True:
        print("+---------------------------------------+")
        print("| Game Statistics Queries               |")
        print("+---------------------------------------+")
        print("| 1. Top Games with Highest Total Shots |")
        print("| 2. Games with Most Hits Combined      |")
        print("| 3. Games with Most Power Play Chances |")
        print("| 4. Most One-Sided Wins                |")
        print("| 5. Back to Main Menu                  |")
        print("+---------------------------------------+")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Returning to Main Menu...")
            break

        queries = [
            # 1. Top Games with Highest Total Shots
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                (gts_away.shots + gts_home.shots) AS total_shots,
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
                total_shots DESC;
            """,
            # 2. Games with Most Hits Combined
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                (gts_away.hits + gts_home.hits) AS total_hits,
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
                total_hits DESC;
            """,
            # 3. Games with Most Power Play Opportunities
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                (gts_away.powerPlayOpportunities + gts_home.powerPlayOpportunities) AS total_power_play_opportunities,
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
                total_power_play_opportunities DESC;
            """,
            # 4. Most One-Sided Wins
            """
            SELECT TOP 10
                g.game_id,
                g.date_time_GMT,
                ABS(gts_away.goals - gts_home.goals) AS goal_difference,
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
                goal_difference DESC;
            """
        ]

        # Validate and execute the selected query
        if choice.isdigit() and 1 <= int(choice) <= 4:
            query = queries[int(choice) - 1]
            execute_query(connection, query)
        else:
            print("Invalid choice. Please select a valid option.")
