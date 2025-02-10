from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, select
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped
from sqlalchemy.orm import mapped_column

# Создаем "мостик" к базе данных (файл mydatabase.db)
engine = create_engine('sqlite:///mydatabase2.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Исправлено на __tablename__
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Указан тип
    name: Mapped[str] = mapped_column(String, nullable=False)  # Указан тип
    age: Mapped[int] = mapped_column(Integer)  # Указан тип
    orders = relationship('Order', backref='user')

class Order(Base):
    __tablename__ = 'orders'  # Исправлено на __tablename__
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Указан тип
    product: Mapped[str] = mapped_column(String)  # Указан тип
    price: Mapped[float] = mapped_column(Float)  # Указан тип
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # Указан тип

# Шаг 5: Создаем таблицы
Base.metadata.create_all(engine)

# Шаг 6: Сессия
Session = sessionmaker(bind=engine)
session = Session()

# Шаг 6: Добавляем пользователя
new_user = User(name="Анна", age=25)
session.add(new_user)
session.commit()

# Шаг 10: Добавляем заказ
user = session.execute(select(User)).scalars().first()
new_order = Order(product="Книга", price=500, user=user)
session.add(new_order)
session.commit()

# Шаг 7: Получаем пользователей
users = session.execute(select(User)).scalars().all()
for user in users:
    print(f"ID: {user.id}, Имя: {user.name}, Возраст: {user.age}")

# Шаг 11: Получаем заказы
user = session.execute(select(User)).scalars().first()
print(f"Заказы пользователя {user.name}:")
for order in user.orders:
    print(f"- {order.product} (Цена: {order.price} руб.)")

# Закрываем сессию
session.close()