from config_loader import connect_to_database
from main_menu import main_menu
from player_menu import player_performance_menu

def main():
    """Main function to handle the interface."""
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to the database. Exiting.")
        return

    while True:
        choice = main_menu()
        if choice == '1':
            player_performance_menu(connection)
        elif choice == '7':  # Exit
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    connection.close()

if __name__ == "__main__":
    main()
