import sqlite3


class DatabaseManager:
    def __init__(self, db_name='mydatabase.db'):
        self.__db_name = db_name  # Исправлено имя переменной

    def __enter__(self):
        self.db = sqlite3.connect(self.__db_name)
        self.c = self.db.cursor()
        self.create_tables()  # Переименовано для создания всех таблиц
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    def create_tables(self):  # Объединено создание таблиц
        # Сначала создаём users
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )''')

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                product TEXT NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        self.db.commit()

    # Остальные методы класса остаются без изменений
    def create_user(self, name: str, age: int):
        self.c.execute('INSERT INTO users (name, age) VALUES (?, ?)',
                       (name, age))
        self.db.commit()

    def get_all_users(self):
        self.c.execute('SELECT * FROM users')
        return self.c.fetchall()

    def update_user_age(self, user_id: int, new_age: int):
        self.c.execute('UPDATE users SET age = ? WHERE id = ?',
                       (new_age, user_id))
        self.db.commit()

    def delete_user(self, user_id: int):
        self.c.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db.commit()

    def create_order(self, user_id: int, product: str, price: float):
        self.c.execute('''
            INSERT INTO orders (user_id, product, price) 
            VALUES (?, ?, ?)
        ''', (user_id, product, price))
        self.db.commit()

    def get_orders_by_user(self, user_id):
        self.c.execute('''SELECT * FROM orders 
                            WHERE user_id = ?''', (user_id,))
        return self.c.fetchall()

    def get_users_with_orders(self):
        self.c.execute('''SELECT users.name, orders.product, orders.price 
                        FROM orders INNER JOIN users on orders.user_id = users.id''')
        return self.c.fetchall()

    def get_total_revenue_by_product(self):
        """Возвращает общую выручку по каждому товару."""
        self.c.execute('''SELECT product, SUM(price) 
                            FROM orders 
                            GROUP BY product''')
        return self.c.fetchall()

    def get_average_order_value(self):
        self.c.execute('''SELECT COALESCE(SUM(price), 0) FROM orders''')
        total_sum = self.c.fetchone()[0]

        self.c.execute('''SELECT COALESCE(count(id), 0) FROM orders''')
        total_orders = self.c.fetchone()[0]

        if total_orders == 0:
            return 0.0
        return total_sum / total_orders