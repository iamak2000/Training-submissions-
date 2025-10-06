import pandas as pd
import pandasql as ps

df = pd.read_csv("data.csv")

query = "SELECT * FROM df;"


result = ps.sqldf(query, locals())

print("--- Query Result ---")
print(result)


query2 = "SELECT Name, Age FROM df WHERE Age > 28;"
result2 = ps.sqldf(query2, locals())

print("\n--- Filtered Result (Age > 28) ---")
print(result2)
