#uv add "psycopg[binary]"

import psycopg
import pandas as pd

def get_connection():
    return psycopg.connect(
        host="localhost",
        port=,
        dbname="financial_data",
        user="",
        password=""
    )

