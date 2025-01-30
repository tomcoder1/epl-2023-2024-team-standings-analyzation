import pandas as pd
url = "https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats"
tables = pd.read_html(url, header=[1]) 
#header = [1] -> Pandas' read_html() detects multiple header rows and interprets them incorrectly.
df = tables[1]
df.to_csv("premier_league_2023_2024.csv", index=False)
print("CSV file saved successfully!")
