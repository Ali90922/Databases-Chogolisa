import sqlite3

# Define the database and SQL script file names
database_file = "products_database.db"
sql_script_file = "products.sql"

# Create and set up the database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

try:
    # Execute the SQL script to create tables and insert data
    with open(sql_script_file, 'r') as file:
        cursor.executescript(file.read())
    conn.commit()
    print("Database and tables created successfully.")
    
    # Part (a): Find people who have NOT purchased at least two items
    query_a = """
    SELECT firstname, lastname
    FROM people
    WHERE personID NOT IN (
        SELECT personID
        FROM orders
        GROUP BY personID
        HAVING COUNT(orderID) >= 2
    );
    """
    print("\nPart (a) Results:")
    cursor.execute(query_a)
    for row in cursor.fetchall():
        print(row)
    
    # Part (b): Find product names for products viewed but not bought, costing $10.00 or less
    query_b = """
    SELECT DISTINCT p.prodName
    FROM products p
    JOIN viewed v ON p.productID = v.productID
    WHERE p.price <= 10.00
      AND NOT EXISTS (
          SELECT 1
          FROM orderLineItems oli
          JOIN orders o ON oli.orderID = o.orderID
          WHERE o.personID = v.personID
            AND oli.productID = v.productID
      );
    """
    print("\nPart (b) Results:")
    cursor.execute(query_b)
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("An error occurred:", e)

# Close the connection
finally:
    conn.close()
