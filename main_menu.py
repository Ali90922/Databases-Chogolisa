def main_menu():
    """Display the main menu and handle navigation."""
    print("+---------------------------------------+")
    print("| NHL Query Interface                   |")
    print("+---------------------------------------+")
    print("| 1. Player Performance                 |")
    print("| 2. Team Performance                   |")
    print("| 3. Game Statistics                    |")
    print("| 4. Event Statistics                   |")
    print("| 5. List All Teams                     |")
    print("| 6. Season Rankings                    |")  # Updated numbering for rankings
    print("| 7. Scratches/Reserves                 |")
    print("| 8. Exit                               |")
    print("+---------------------------------------+")
    choice = input("Enter your choice: ")
    return choice
