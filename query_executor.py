def execute_query(connection, query, parameters=None):
    """Execute a SQL query and print the results."""
    try:
        cursor = connection.cursor(as_dict=True)
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Failed to execute query. Error:", e)

