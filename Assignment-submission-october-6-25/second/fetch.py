import sqlite3
import pandas as pd


df = pd.read_csv('data.csv')


conn = sqlite3.connect(':memory:')


df.to_sql('data_table', conn, index=False, if_exists='replace')


query = 'SELECT * FROM data_table WHERE Age > 30;'
result = pd.read_sql_query(query, conn)

print(result)

conn.close()