def execute_query(connection, query):
    """Execute a SQL query and print the results."""
    try:
        cursor = connection.cursor(as_dict=True)
        cursor.execute(query)
        results = cursor.fetchall()

        # Print results in a readable format
        for row in results:
            print(row)
    except Exception as e:
        print("Failed to execute query. Error:", e)
