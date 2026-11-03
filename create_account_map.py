from connection import get_connection
from sqlalchemy import create_engine
import pandas as pd


df = pd.read_excel('dataset import/account_mapping.xlsx')

engine = create_engine(
    'postgresql+psycopg2://username:password@localhost:/financial_data'
)

df.to_sql(
    name='account_mapping',
    con=engine,
    if_exists='replace',
    index=False
)