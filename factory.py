import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime
import bcrypt


load_dotenv()

#DATABASE CREDENTIALS
DB_HOST = os.getenv("DATABASE_HOST")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_USER = os.getenv("DATABASE_USERNAME")
DB_NAME = os.getenv("DATABASE_NAME")


class DatabaseFactory:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connection to MySQL DB successful")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection = None

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")

    def add_data(self, data_list):
        if self.connection is None:
            print("Connection is not established.")
            return

        try:
            cursor = self.connection.cursor()
            for entry in data_list:
                table = entry['table']
                rows = entry['data']
                
                for row in rows:
                    placeholders = ", ".join(["%s"] * len(row))
                    columns = ", ".join(row.keys())
                    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                    cursor.execute(sql, list(row.values()))
                    print(f"Data added to {table} successfully.")
                self.connection.commit()
        except Error as e:
            print(f"Error: '{e}'")
        finally:
            cursor.close()


if __name__ == "__main__":
    db = DatabaseFactory(host=DB_HOST, database=DB_NAME, 
                         user=DB_USER, password=DB_PASS)
    db.create_connection()

    
    data_to_add = [
        {
            'table': 'authors',
            'data': 
                [
                    {
                    'name': 'John Doe',
                    'description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
                    'created_at': datetime.utcnow()
                    },

                    {
                    'name': 'Arnold Bennett',
                    'description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
                    'created_at': datetime.utcnow()
                    },
                    {
                    'name': 'A. E. Coppard',
                    'description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
                    'created_at': datetime.utcnow()
                    },
                ]

          
        },
        {
            'table': 'book_categories',
            'data': 
            [
                    {
                    'name': 'Story',
                    'slug': 'story',
                    'created_at': datetime.utcnow()
                    },
                    {
                    'name': 'Novel',
                    'slug': 'novel',
                    'created_at': datetime.utcnow()
                    },
                    {
                    'name': 'Academic',
                    'slug': 'academic',
                    'created_at': datetime.utcnow()
                    }
            ]
        },
        {
            'table': 'users',
            'data':             
            [       #admin credentials
                    { 
                    'name': 'admin',
                    'email': 'admin@filament.com',
                    'password' : bcrypt.hashpw(b'admin123', bcrypt.gensalt()),
                    'role' : 1,
                    'created_at': datetime.utcnow()
                    },
                    #student credentials
                    {
                    'name': 'Hanzala Afzal',
                    'email': 'hanzala@filament.com',
                    'password' : bcrypt.hashpw(b'hanzala123', bcrypt.gensalt()),
                    'role' : 1,
                    'created_at': datetime.utcnow()
                    },
                    {
                    'name': 'Martin Klug',
                    'email': 'martin@filament.com',
                    'password' : bcrypt.hashpw(b'martin123', bcrypt.gensalt()),
                    'role' : 1,
                    'created_at': datetime.utcnow()
                    }
            ]
        }
    ]

    db.add_data(data_to_add)
    db.close_connection()