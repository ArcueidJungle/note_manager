import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from SQLALCHMY import User


reader = pd.read_csv
reader = reader[reader['age'] > 0]
reader.drop_duplicates(subset=["email"], keep="first", inplace=True)

engine = create_engine('sqlite:///mydatabase2.db')
Session = sessionmaker(bind = engine)
session = Session()


# 4. Сохранение данных
for index, row in reader.iterrows():
    user = User(
        name=row["name"],
        email=row["email"],
        age=row["age"]
    )
    session.add(user)

session.commit()
session.close()  # Важно!