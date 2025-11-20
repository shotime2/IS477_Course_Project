import pandas as pd

df = pd.read_csv("/Users/shovraman/IS477_Course_Project/raw/raw_air_quality.csv")

df = df[["state_code", "parameter", "arithmetic_mean", "year"]]
pollutants = {
    '88101': 'PM25_mean',
    '44201': 'Ozone_mean',
    '42101': 'CO_mean'
}
df = df[df["parameter"].isin(pollutants.keys())]

df = df[(df['year'] >= 2014) & (df['year'] <= 2024)]

state_map = {
    '01':'AL','02':'AK','04':'AZ','05':'AR','06':'CA','08':'CO','09':'CT','10':'DE',
    '12':'FL','13':'GA','15':'HI','16':'ID','17':'IL','18':'IN','19':'IA','20':'KS',
    '21':'KY','22':'LA','23':'ME','24':'MD','25':'MA','26':'MI','27':'MN','28':'MS',
    '29':'MO','30':'MT','31':'NE','32':'NV','33':'NH','34':'NJ','35':'NM','36':'NY',
    '37':'NC','38':'ND','39':'OH','40':'OK','41':'OR','42':'PA','44':'RI','45':'SC',
    '46':'SD','47':'TN','48':'TX','49':'UT','50':'VT','51':'VA','53':'WA','54':'WV',
    '55':'WI','56':'WY'
}
df['State'] = df['state_code'].astype(str).map(state_map)

df = df.dropna(subset=['State'])
df['parameter'] = df['parameter'].map(pollutants)

df_grouped = df.groupby(['State', 'year', 'parameter'])['arithmetic_mean'].mean().reset_index()
df_final = df_grouped.pivot(index=['State', 'year'],columns='parameter', values='arithmetic_mean').reset_index()

df_final.to_csv("/Users/shovraman/IS477_Course_Project/clean/air_state_year_clean.csv",index=False)
