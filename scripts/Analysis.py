import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/Users/shovraman/IS477_Course_Project/merged/merged_ev_and_air.csv")
df_2014 = df[df["year"] == 2014]
df_2023 = df[df["year"] == 2023]


merged = df_2014.merge(df_2023, on="State", suffixes=("_2014", "_2023"))


merged["ev_growth"] = merged["ev_station_count_2023"] - merged["ev_station_count_2014"]
merged["pm25_change"] = merged["PM2.5 - Local Conditions_2023"] - merged["PM2.5 - Local Conditions_2014"]
merged["ozone_change"] = merged["Ozone_2023"] - merged["Ozone_2014"]


correlation_table = merged[["ev_growth", "pm25_change", "ozone_change"]].corr()
print(correlation_table)

correlation_table.to_csv("/Users/shovraman/IS477_Course_Project/analysis/correlation_table.csv")

plt.figure(figsize=(10, 7))
plt.scatter(merged["ev_growth"], merged["pm25_change"])
for i in range(len(merged)):
    plt.text(merged["ev_growth"].iloc[i] + 3, 
             merged["pm25_change"].iloc[i] + 0.02, 
             merged["State"].iloc[i], 
             fontsize=8)
plt.xlabel("EV Growth (2014–2023)")
plt.ylabel("PM2.5 Change")
plt.title("EV Growth vs PM2.5 Change")
plt.grid(alpha=0.3)
plt.savefig("/Users/shovraman/IS477_Course_Project/analysis/PM25_scatterplot.png")
plt.show()


plt.figure(figsize=(10, 7))
plt.scatter(merged["ev_growth"], merged["ozone_change"])
for i in range(len(merged)):
    plt.text(
        merged["ev_growth"].iloc[i] + 3,
        merged["ozone_change"].iloc[i] + 0.0002,  
        merged["State"].iloc[i],
        fontsize=8)
plt.xlabel("EV Growth (2014–2023)")
plt.ylabel("Ozone Change")
plt.title("EV Growth vs Ozone Change")
plt.grid(alpha=0.3)
plt.savefig("/Users/shovraman/IS477_Course_Project/analysis/Ozone_scatterplot.png")
plt.show()


