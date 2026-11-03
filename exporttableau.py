import pandas as pd
from connection import get_connection
conn = get_connection()

def fetch_data(query):
    try:
        with conn:
            df = pd.read_sql(query, conn)
            df.to_csv('CSVS/fact_trans_month.csv', index=False)
            print("It worked")
    except:
        print("Did not work")
    finally:
        conn.close()
    return df

Query = """select * from fact_trans_month;"""
#"""select * from dim_date;"""
#"""select * from dim_stores;"""
#"""select * from dim_stores;"""
#"""select * from dim_account_mapping;"""
#"""select * from dim_accounts;"""

fetch_data(Query)