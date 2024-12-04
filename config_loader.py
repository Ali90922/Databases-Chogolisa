import pymssql
import configparser

def load_config():
    """Load database credentials from auth.config."""
    config = configparser.ConfigParser()
    config.read("auth.config")
    return config["database"]

def connect_to_database():
    """Establish a connection to the database using credentials from auth.config."""
    config = load_config()
    try:
        connection = pymssql.connect(
            server=config["server"],
            user=config["username"],
            password=config["password"],
            database=config["database"]
        )
        print("Connected to the database successfully!")
        return connection
    except Exception as e:
        print("Failed to connect to the database. Error:", e)
        return None

