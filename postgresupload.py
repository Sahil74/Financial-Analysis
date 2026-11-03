import duckdb
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://username:password@localhost:/financial_data"

engine = create_engine(DATABASE_URL)

# Connect to DuckDB
con = duckdb.connect(
    "data.duckdb",
    read_only=True
)

try:
    tables = con.execute("SHOW TABLES").fetchdf()["name"].tolist()

    print(f"Found {len(tables)} tables: {tables}")

    for table in tables:
        print(f"\nImporting: {table}")

        df = con.execute(
            f'SELECT * FROM "{table}"'
        ).fetchdf()

        df.to_sql(
            name=table,
            con=engine,
            schema="public",
            if_exists="fail",
            index=False,
            chunksize=1000
        )

        print(f"Imported {len(df):,} rows")

finally:
    con.close()
    engine.dispose()

print("\nAll tables imported successfully!")
