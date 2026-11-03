from connection import get_connection
conn = get_connection()

def execute(query):
    try:
        with conn:
            conn.execute(query)
            print("done")
    finally:
        conn.close()

Query = """create table dim_account_mapping AS select account_number, account_name, pl_line , statement_type, sort_order, notes FROM account_mapping_second order by sort_order, account_number;"""
#"""create table dim_stores AS select store_code, store_name, store_type, country, region from stores_second order by store_code;"""
#"""create table dim_accounts AS select account_number, account_name, account_type, currency from account_second order by account_number"""
execute(Query)