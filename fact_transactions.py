from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
            print("done")
    finally:
        conn.close()


Query = """create table fact_transactions as select transaction_id, transaction_date, store_code, account_number, amount_local, currency, document_number, description from transactions_second order by transaction_id"""
execute(Query)