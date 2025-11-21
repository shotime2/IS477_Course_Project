import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/creid317/IS 477 Project/IS477_Course_Project/merged/merged_ev_and_air.csv")
df_corr = df[["ev_station_count", "Carbon monoxide", "Ozone", "PM2.5 - Local Conditions"]]
correlation_matrix = df_corr.corr()
correlation_matrix.to_csv("/Users/creid317/IS 477 Project/IS477_Course_Project/Analysis/correlation_matrix.csv", index=True)

plt.scatter(df["ev_station_count"], df["Carbon monoxide"])
plt.xlabel("EV Charging Station Count")
plt.ylabel("Carbon Monoxide")
plt.title("EV Stations vs Carbon Monoxide")
plt.savefig("/Users/creid317/IS 477 Project/IS477_Course_Project/Analysis/EV_vs_CM.png")
plt.show()

plt.scatter(df["ev_station_count"], df["Ozone"])
plt.xlabel("EV Charging Station Count")
plt.ylabel("Ozone")
plt.title("EV Stations vs Ozone")
plt.savefig("/Users/creid317/IS 477 Project/IS477_Course_Project/Analysis/EV_vs_OZ.png")
plt.show()

plt.scatter(df["ev_station_count"], df["PM2.5 - Local Conditions"])
plt.xlabel("EV Charging Station Count")
plt.ylabel("PM2.5 - Local Conditions")
plt.title("EV Stations vs PM2.5")
plt.savefig("/Users/creid317/IS 477 Project/IS477_Course_Project/Analysis/EV_vs_PM.png")
plt.show()
