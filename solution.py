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

df = df[df["product"] == "Pink Morsel"]

df["sales"] = df["quantity"] * df["price"]

df = df[["sales", "date", "region"]]

df.to_csv(output_file, index=False)
print("Done! Output saved to", output_file)
