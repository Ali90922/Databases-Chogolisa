import subprocess
import configparser

def execute_sql_file(sql_file, server, database, username, password, batch_size=30000):
    """
    Execute a SQL file in batches using sqlcmd.
    :param sql_file: Path to the SQL file.
    :param server: MSSQL server address.
    :param database: Target database name.
    :param username: Username for MSSQL authentication.
    :param password: Password for MSSQL authentication.
    :param batch_size: Number of lines to execute per batch (default: 30000).
    """
    try:
        # Read the SQL file content
        with open(sql_file, "r") as file:
            sql_content = file.readlines()
        # Split the SQL content into batches
        batch = []
        for i, line in enumerate(sql_content):
            batch.append(line)
            # If batch size is reached or it's the last line, execute the batch
            if (i + 1) % batch_size == 0 or i == len(sql_content) - 1:
                batch_sql = "".join(batch)
                execute_batch(batch_sql, server, database, username, password)
                batch = []  # Clear the batch after execution
        print(f"{sql_file} executed successfully.")
    except Exception as e:
        print(f"Error while executing {sql_file}: {e}")

def execute_batch(batch_sql, server, database, username, password):
    """
    Execute a single batch of SQL commands using sqlcmd.
    :param batch_sql: SQL commands as a string.
    :param server: MSSQL server address.
    :param database: Target database name.
    :param username: Username for MSSQL authentication.
    :param password: Password for MSSQL authentication.
    """
    # Write the batch SQL to a temporary file
    temp_file = "temp_batch.sql"
    with open(temp_file, "w") as temp:
        temp.write(batch_sql)
    # Construct the sqlcmd command
    command = [
        "sqlcmd",
        "-S", server,
        "-d", database,
        "-U", username,
        "-P", password,
        "-i", temp_file
    ]
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print("Batch executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing batch: {e}")
    finally:
        # Clean up the temporary file
        import os
        if os.path.exists(temp_file):
            os.remove(temp_file)

def load_credentials(config_file):
    """
    Load database credentials from a config file.
    :param config_file: Path to the config file.
    :return: Dictionary containing server, database, username, and password.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    db_config = config["database"]
    return db_config["server"], db_config["database"], db_config["username"], db_config["password"]

# Configuration
config_file = "auth.config"  # Path to your config file

# SQL file paths
drop_sql_file = "drop.sql"  # Path to your DROP script
create_table_sql_file = "create_table.sql"  # Path to your CREATE TABLE script
insert_sql_file = "insert.sql"  # Path to your INSERT script

# Load credentials from the config file
server, database, username, password = load_credentials(config_file)

# Execute the DROP script first
execute_sql_file(drop_sql_file, server, database, username, password)

# Execute the CREATE TABLE script
execute_sql_file(create_table_sql_file, server, database, username, password)

# Execute the INSERT script
execute_sql_file(insert_sql_file, server, database, username, password)
