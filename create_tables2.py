from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
            print("done")
    finally:
        conn.close()

Query= """CREATE TABLE transactions_second AS SELECT store_code, transaction_id, TO_CHAR(transaction_date, 'DD.MM.YYYY') AS transaction_date, account_number, amount_local, UPPER(TRIM(currency)) AS currency, document_number, TRIM(description) AS description FROM transactions_first;"""
#Query = """create table stores_second AS select s.store_code, TRIM(s.store_name) AS store_name, UPPER(TRIM(s.store_type)) AS store_type, g.country, g.region from stores_first s LEFT JOIN geography_first g ON s.store_code = g.store_code;"""
#Query = """create table account_second AS select CAST(account_number AS INTEGER) AS account_number, TRIM(account_name) AS account_name, UPPER(TRIM(account_type)) AS account_type, UPPER(TRIM(currency)) AS currency from account_first;"""
#Query = """create table account_mapping_second AS select CAST("AccountNumber" AS INTEGER) AS account_number, TRIM("AccountName") AS account_name, TRIM("PLLine") AS pl_line , UPPER(TRIM("StatementType")) AS statement_type, CAST("SortOrder" AS INTEGER) AS sort_order, TRIM("Notes") AS notes FROM account_mapping;"""
execute(Query)

