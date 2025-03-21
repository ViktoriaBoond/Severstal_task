from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = 'sqlite:///./metal_rolls.db'    # Определение URL базы данных

engine = create_engine(SQL_DB_URL, connect_args={'check_same_thread': False})    # Создание движка базы данных

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)    # Создание фабрики сессий

Base = declarative_base()    # Создание базового класса для моделей




