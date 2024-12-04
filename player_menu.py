from query_executor import execute_query

def general_stats_menu(connection):
    """Display the General Stats submenu and execute queries with prepared statements."""
    while True:
        print("+---------------------------------------+")
        print("| General Stats Queries                 |")
        print("+---------------------------------------+")
        print("| 1. Top Scorers                        |")
        print("| 2. Most Penalty Minutes by Team       |")
        print("| 3. Most Game-Winning Goals            |")
        print("| 4. Top Performers by Birth City       |")
        print("| 5. Most Assists in Power Play         |")
        print("| 6. Best Face-Off Win Percentage       |")
        print("| 7. Most Time on Ice                   |")
        print("| 8. Best Save Percentage               |")
        print("| 9. Most Takeaways                     |")
        print("| 10. Back to Player Performance Menu   |")
        print("+---------------------------------------+")
        
        choice = input("Enter your choice: ")

        if choice == '10':
            print("Returning to Player Performance Menu...")
            break

        # Mapping of queries
        queries = [
            # 1. Top Scorers
            """
            SELECT TOP 10
                pi.firstName, 
                pi.lastName, 
                SUM(gss.goals) AS total_goals
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            JOIN 
                game g ON gss.game_id = g.game_id
            GROUP BY 
                pi.firstName, pi.lastName
            ORDER BY 
                total_goals DESC;
            """,
            # 2. Most Penalty Minutes by Team
            """
            SELECT TOP 10
                ti.teamName,
                pi.firstName,
                pi.lastName,
                SUM(gss.penaltyMinutes) AS total_penalty_minutes
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            JOIN 
                team_info ti ON gss.team_id = ti.team_id
            GROUP BY 
                ti.teamName, pi.firstName, pi.lastName
            ORDER BY 
                total_penalty_minutes DESC;
            """,
            # 3. Most Game-Winning Goals
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                COUNT(gg.play_id) AS game_winning_goals
            FROM 
                game_goals gg
            JOIN 
                Performs p ON gg.play_id = p.play_id
            JOIN 
                player_info pi ON p.player_id = pi.player_id
            WHERE 
                gg.gameWinningGoal = 1
            GROUP BY 
                pi.firstName, pi.lastName
            ORDER BY 
                game_winning_goals DESC;
            """,
            # 4. Top Performers by Birth City
            """
            SELECT TOP 10
                pi.birthCity,
                pi.firstName,
                pi.lastName,
                SUM(gss.goals) AS total_goals
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            GROUP BY 
                pi.birthCity, pi.firstName, pi.lastName
            HAVING 
                SUM(gss.goals) > 10
            ORDER BY 
                total_goals DESC;
            """,
            # 5. Most Assists in Power Play
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                SUM(gss.powerPlayAssists) AS total_power_play_assists
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            GROUP BY 
                pi.firstName, pi.lastName
            ORDER BY 
                total_power_play_assists DESC;
            """,
            # 6. Best Face-Off Win Percentage
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                SUM(gss.faceOffWins) AS total_face_off_wins,
                SUM(gss.faceoffTaken) AS total_faceoffs_taken,
                (SUM(gss.faceOffWins) * 100.0 / SUM(gss.faceoffTaken)) AS win_percentage
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            GROUP BY 
                pi.firstName, pi.lastName
            HAVING 
                SUM(gss.faceoffTaken) > 50
            ORDER BY 
                win_percentage DESC;
            """,
            # 7. Most Time on Ice
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                SUM(gss.timeOnIce) AS total_time_on_ice
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            GROUP BY 
                pi.firstName, pi.lastName
            ORDER BY 
                total_time_on_ice DESC;
            """,
            # 8. Best Save Percentage
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                SUM(ggs.saves) AS total_saves,
                SUM(ggs.shots) AS total_shots,
                (SUM(ggs.saves) * 100.0 / SUM(ggs.shots)) AS save_percentage
            FROM 
                game_goalie_stats ggs
            JOIN 
                player_info pi ON ggs.player_id = pi.player_id
            GROUP BY 
                pi.firstName, pi.lastName
            HAVING 
                SUM(ggs.shots) >= 100
            ORDER BY 
                save_percentage DESC;
            """,
            # 9. Most Takeaways
            """
            SELECT TOP 10
                pi.firstName,
                pi.lastName,
                SUM(gss.takeaways) AS total_takeaways
            FROM 
                game_skater_stats gss
            JOIN 
                player_info pi ON gss.player_id = pi.player_id
            GROUP BY 
                pi.firstName, pi.lastName
            ORDER BY 
                total_takeaways DESC;
            """
        ]

        # Validate and execute the selected query
        if choice.isdigit() and 1 <= int(choice) <= 9:
            query = queries[int(choice) - 1]
            execute_query(connection, query, parameters=())  # No parameters are passed in these queries
        else:
            print("Invalid choice. Please select a valid option.")


def player_performance_menu(connection):
    """Display the Player Performance Queries submenu."""
    while True:
        print("+---------------------------------------+")
        print("| Player Performance Queries            |")
        print("+---------------------------------------+")
        print("| 1. General Stats                      |")
        print("| 2. Back to Main Menu                  |")
        print("+---------------------------------------+")
        
        choice = input("Enter your choice: ")

        if choice == '2':
            print("Returning to Main Menu...")
            break
        elif choice == '1':
            general_stats_menu(connection)
        else:
            print("Invalid choice. Please select a valid option.")
