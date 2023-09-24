'''
This file contains the Database class that handles the database connection and operations.
'''
import psycopg2
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_username",
            password="your_password"
        )
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        '''
        This method creates the "users" table if it doesn't exist.
        '''
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(100)
        )
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()
    def save_user(self, first_name, last_name, email):
        '''
        This method saves the user's information into the database.
        '''
        insert_query = '''
        INSERT INTO users (first_name, last_name, email)
        VALUES (%s, %s, %s)
        '''
        self.cursor.execute(insert_query, (first_name, last_name, email))
        self.conn.commit()
    def close_connection(self):
        '''
        This method closes the database connection and cursor objects.
        '''
        self.cursor.close()
        self.conn.close()