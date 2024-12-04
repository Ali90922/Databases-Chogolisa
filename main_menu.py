def main_menu():
    """Display the main menu and handle navigation."""
    print("+---------------------------------------+")
    print("| NHL Query Interface                   |")
    print("+---------------------------------------+")
    print("| 1. Player Performance Queries         |")
    print("| 2. Team Performance Queries           |")
    print("| 3. Game Statistics Queries            |")  # Updated here
    print("| 4. Officiating Trends Queries         |")
    print("| 5. List All Teams                     |")
    print("| 6. Custom Query                       |")
    print("| 7. Exit                               |")
    print("+---------------------------------------+")
    choice = input("Enter your choice: ")
    return choice
