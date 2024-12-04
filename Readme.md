# Databases-Chogolisa

![Alt text](Jets.png)

## Database Concepts and Design CG 47 - Ali - Rayan - Singh

### How to Populate the Database

1. **Ensure you have the necessary files:**
    - `create-table.sql`: Contains the SQL commands to create the necessary tables.
    - `dump.sql`: Contains the unsorted `INSERT` statements to populate the tables.
    - `reorder_script.py`: Script to sort the `INSERT` statements.
    - `batch_script2.py`: Script to upload the sorted SQL file to the Uranium server in small batches.

2. **Configure the database connection:**
    - Edit the `auth.config` file with your database credentials:
      ```plaintext
      [database]
      server = uranium.cs.umanitoba.ca
      database = cs3380
      username = your_username
      password = your_password
      ```

3. **Sort the `INSERT` statements:**
    - Ensure you have Python installed.
    - Run the `reorder_script.py` script to sort the `INSERT` statements:
      ```sh
      python reorder_script.py
      ```

4. **Run the `batch_script2.py` to create tables and populate the database:**
    - Ensure you have Python installed.
    - Install the required Python packages:
      ```sh
      pip install pymssql
      ```
    - Run the `batch_script2.py` script:
      ```sh
      python batch_script2.py
      ```

### How to Run the Interface

1. **Ensure you have the necessary files:**
    - `interface.py`: Contains the code for the interface.
    - `auth.config`: Contains your database credentials.

2. **Run the `interface.py` script:**
    - Ensure you have Python installed.
    - Install the required Python packages:
      ```sh
      pip install pymssql
      ```
    - Run the `interface.py` script:
      ```sh
      python interface.py
      ```

3. **Use the interface:**
    - Follow the on-screen instructions to navigate through the menu and execute queries.

### Example Commands

- **Sort `INSERT` statements:**
     ```sh
     python reorder_script.py
     ```

- **Create tables and populate database:**
     ```sh
     python batch_script2.py
     ```

- **Run the interface:**
     ```sh
     python interface.py
     ```

Make sure to replace `your_username` and `your_password` with your actual database credentials.

This `README.md` file now includes instructions for sorting the `INSERT` statements using `reorder_script.py`, and then using `batch_script2.py` to create tables and populate the database. It also includes instructions on how to run the interface.