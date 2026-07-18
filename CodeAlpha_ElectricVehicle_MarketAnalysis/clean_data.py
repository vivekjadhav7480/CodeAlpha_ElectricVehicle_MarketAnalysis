import pandas as pd

# Load scraped dataset
df = pd.read_csv("dataset/scraped_ev_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where Model is missing
df = df.dropna(subset=["Model"])

# Remove extra spaces
df["Model"] = df["Model"].str.strip()

# Save cleaned dataset
df.to_csv("dataset/cleaned_scraped_ev_data.csv", index=False)

print("Cleaning Completed Successfully!")
print(df.head())