import pandas as pd

ev_data = pd.read_csv("clean/ev_state_year_clean.csv")
air_data = pd.read_csv("clean/air_state_year_clean.csv")

df_merge = pd.merge(ev_data, air_data, on = ["State", "year"], how = "inner")
df_merge.to_csv("merged/merged_ev_and_air.csv", index=False)