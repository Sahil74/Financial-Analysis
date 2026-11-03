import duckdb
from sqlalchemy import create_engine

con = duckdb.connect("data.duckdb", read_only=True)

#tables and datas
tables = con.execute("SHOW TABLES").fetchall()
for (table,) in tables:
    count = con.execute(
        f'SELECT COUNT(*) FROM "{table}"'
    ).fetchone()[0]

    print(f"{table}: {count:,} rows")

print(con.execute("""
    DESCRIBE transactions_data
""").fetchdf())

print(con.execute("""
    SELECT *
    FROM transactions_data
    LIMIT 10
""").fetchdf().to_string(index=False))
con.close()



DATABASE_URL = "postgresql+psycopg2://username:password@localhost:/financial_data"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    print("Successfully connected to PostgreSQL!")