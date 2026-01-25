import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_FILE = "all_urls.csv"

dfs = []

for csv_file in DATA_DIR.glob("*.csv"):
    print(f"Reading {csv_file}")
    df = pd.read_csv(csv_file)
    df["source_file"] = csv_file.name  # optional but useful
    dfs.append(df)

# Combine all CSVs
combined_df = pd.concat(dfs, ignore_index=True)

# Ensure string type before combining
combined_df["GAME_HISTORY_ID"] = (
    combined_df["api_game_id"].astype(str) +
    combined_df["action_number"].astype(str)
)

# Save output
combined_df.to_csv(OUTPUT_FILE, index=False)
print(combined_df.head(30))
print(f"\nSaved {len(combined_df):,} rows to {OUTPUT_FILE}")
