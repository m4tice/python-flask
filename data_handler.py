import sqlite3
import randomname
import numpy as np

connection = sqlite3.connect('./app/data.db')
cursor = connection.cursor()

# Query to check if the 'users' table exists
check_table_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"

cursor.execute(check_table_query)
table_exists = cursor.fetchone()

if table_exists:
    # Adding a new user to the 'users' table if table already exists
    print("Table 'users' already exists. Adding a new user...")
    for i in range(10):
        name = str(randomname.get_name())
        age = str(np.random.randint(18, 60))
        params = (name, age)
        add_user_query = f"INSERT INTO users (name, age) VALUES (?, ?)"

        # query to insert data into the 'users' table
        cursor.execute(add_user_query, params)
        connection.commit()
else:
    # Create the 'users' table if it does not exist
    create_table_query = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    cursor.execute(create_table_query)
    print("Table 'users' created.")

# Example query to fetch data from the 'users' table
fetch_data_query = "SELECT * FROM users"
cursor.execute(fetch_data_query)
data = cursor.fetchall()

connection.close()

# Print fetched data
for row in data:
    print("row:", row)