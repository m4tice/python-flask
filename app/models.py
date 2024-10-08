"""This file can be used to define database models"""

# from app import app

import sqlite3
import randomname
import numpy as np

class DataDB:
    def __init__(self):
        self.connection = sqlite3.connect("app/data.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.table_name = 'users'
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
        self.connection.commit()

    def add_data(self, data):
        self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (data))
        self.connection.commit()

    def add_random_data(self):
        name = randomname.get_name()
        age = np.random.randint(0, 100)
        params = (name, age)
        self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', params)
        self.connection.commit()

    def get_data(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        data = []
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'age': row[2]
            })
        return data

    # def __del__(self):
    #     self.connection.close()

    def close(self):
        self.connection.close()
