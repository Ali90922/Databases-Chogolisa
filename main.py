from player_menu import player_performance_menu

def main():
    """Main function to handle the interface."""
    connection = connect_to_database()
    if not connection:
        return

    while True:
        choice = main_menu()
        if choice == '1':
            player_performance_menu(connection)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Feature not implemented yet. Stay tuned!")

    connection.close()
