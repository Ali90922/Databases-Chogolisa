# Databases-Chogolisa

![Alt text](Jets.png)

## Database Concepts and Design CG 47 - Ali - Rayan - Singh

### How to Populate the Database

1. **Ensure you have the necessary files:**
   - `create-table.sql`: Contains the SQL commands to create the necessary tables.
   - `sorted_nhl2.sql`: Contains the sorted `INSERT` statements to populate the tables.

2. **Configure the database connection:**
   - Edit the `auth.config` file with your database credentials:
     ```plaintext
     [database]
     server = uranium.cs.umanitoba.ca
     database = cs3380
     username = your_username
     password = your_password
     ```

3. **Run the `create-table.sql` script to create the tables:**
   - Use the `sqlcmd` utility to execute the `create-table.sql` script:
     ```sh
     sqlcmd -S uranium.cs.umanitoba.ca -d cs3380 -U your_username -P your_password -i create-table.sql
     ```

4. **Run the `batch_script2.py` to populate the tables:**
   - Ensure you have Python installed.
   - Install the required Python packages:
     ```sh
     pip install pymssql
     ```
   - Run the [batch_script2.py](http://_vscodecontentref_/0) script:
     ```sh
     python batch_script2.py
     ```

### How to Run the Interface

1. **Ensure you have the necessary files:**
   - `interface.py`: Contains the code for the interface.
   - [auth.config](http://_vscodecontentref_/1): Contains your database credentials.

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

- **Create tables:**
  ```sh
  sqlcmd -S uranium.cs.umanitoba.ca -d cs3380 -U your_username -P your_password -i create-table.sql

  