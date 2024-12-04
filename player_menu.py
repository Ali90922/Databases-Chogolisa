def player_performance_menu():
    """Display the Player Performance Queries submenu."""
    while True:
        print("+---------------------------------------+")
        print("| Player Performance Queries            |")
        print("+---------------------------------------+")
        print("| 1. Top Scorers (Filter by Season)     |")
        print("| 2. Penalty Minutes (Filter by Team)   |")
        print("| 3. Most Game-Winning Goals            |")
        print("| 4. Player Trends Over Seasons         |")
        print("| 5. Top Performers by Birth City       |")
        print("| 6. Back to Main Menu                  |")
        print("+---------------------------------------+")
        
        choice = input("Enter your choice: ")

        if choice == '6':
            print("Returning to Main Menu...")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            print(f"You selected option {choice}. Feature coming soon!")
        else:
            print("Invalid choice. Please select a valid option.")

