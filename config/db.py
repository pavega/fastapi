from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker


#conexion de python con la base de datos
db_url = "mysql://bf4a4d0ef25e83:b357525a@us-cdbr-east-06.cleardb.net/heroku_ac2340c87509c5a"
meta = MetaData()
engine = create_engine(db_url)
conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)