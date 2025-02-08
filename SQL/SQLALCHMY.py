from sqlalchemy import create_engine

# Создаем "мостик" к базе данных (файл mydatabase.db)
engine = create_engine('sqlite:///mydatabase.db')