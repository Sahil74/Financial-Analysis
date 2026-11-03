from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
    finally:
        conn.close()

Query = """create table stores_first AS select store_code, store_name, store_type from raw__stores_light;"""
#"""create table transactions_first AS select transaction_id, transaction_date, store_code, account_number, amount_local, currency, document_number, description from raw__gl_transactions_light;"""
#"""create table account_first AS select account_number, account_name, account_type, currency from raw__accounts_light;"""
#"""create table geography_first AS select store_code, country, region from raw__geography_light;"""
execute(Query)