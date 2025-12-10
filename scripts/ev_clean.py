import pandas as pd

raw_path = "raw/ev_raw.csv"

df = pd.read_csv(raw_path)

df = df[['ID', 'Latitude', 'Country', 'ZIP', 'Longitude', 'Station Name', 'EV Connector Types', 'Open Date', 'City', 'EV Network', 'State', 'Fuel Type Code']]

df = df[df["Fuel Type Code"] == "ELEC"]
df = df.dropna(subset=["State", "Latitude", "Longitude", "Open Date", "Station Name"])

df["Open Date"] = pd.to_datetime(df["Open Date"], errors= 'coerce')
df["year"] = df["Open Date"].dt.year

df = df[(df["year"] >= 2014) & (df["year"] <= 2024)]

df = df.drop_duplicates(subset= ["ID", "Station Name", "Latitude", "Longitude"])

us_states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL',
             'IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT',
             'NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI',
             'SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

df = df[df["State"].isin(us_states)]

ev_state_year = df.groupby(["State", "year"]).size().reset_index(name = "ev_station_count")

ev_state_year.to_csv("clean/ev_state_year_clean.csv",index=False)



