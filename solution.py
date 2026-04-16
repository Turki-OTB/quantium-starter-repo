import pandas as pd
import os

data_folder = "data"
output_file = "daily_sales.csv"

dfs = []
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        df = pd.read_csv(os.path.join(data_folder, filename))
        dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv(output_file, index=False)
print("Done! Rows:", len(df))
