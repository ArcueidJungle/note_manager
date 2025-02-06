import sqlite3

class DatabaseManager:
        def __init__(self, db_name = 'mydatabase.db'):
            self.__da =db_name

        def __enter__(self):
            self.db = sqlite3.connect(self.__da)
            self.c = self.db.cursor()
            self.create_table()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.db.close()

        def create_table(self):
            self.c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
                )''')
            self.db.commit()


        def create_user(self, name: str, age: int):
            self.c.execute('INSERT INTO users (name, age) values (?, ?)',
                           (name, age)
                           )
            self.db.commit()

        def get_all_users(self):
            self.c.execute('SELECT * FROM users')
            return self.c.fetchall()

        def update_user_age(self, user_id: int, new_age: int):
            self.c.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
            self.db.commit()

        def delete_user(self, user_id: int):
                self.c.execute("DELETE FROM users WHERE id = ?", (user_id,))
                self.db.commit()
