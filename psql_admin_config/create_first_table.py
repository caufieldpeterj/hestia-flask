from sqlalchemy import *
from config import host, port, database, user, password

conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()
print(metadata)

# first_tb = Table('first_table', metadata,
#    Column('id', Integer, primary_key=True),
#    Column('bedrooms', Integer, nullable=False),
#    Column('bathrooms', Integer, nullable=False),
#    Column('sq_ft', Integer, nullable=False),
#    Column('price', Integer, nullable=False),
#    Column('city', String(255), nullable=False),
#    Column('state', String(255), nullable=False),
# )

# metadata.create_all(engine)
# query = insert(first_tb).values(id=1, bedrooms="2", bathrooms=2, sq_ft=350, price=250000, city='Boca Raton', state='Florida')
# ResultProxy = connection.execute(query)