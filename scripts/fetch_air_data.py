import requests
import pandas as pd
import time

API_KEY = "YOUR_KEY"
EMAIL = "YOUR_EMAIL"

POLLUTANTS = {
    "PM2.5": "88101",
    "Ozone": "44201",
    "CO": "42101"
}

years = range(2014, 2024)

df_ev = pd.read_csv("clean/ev_state_year_clean.csv")
states = sorted(df_ev["State"].unique())


state_to_codes = {
    'AL': '01','AK': '02','AZ': '04','AR': '05','CA': '06','CO': '08',
    'CT': '09','DE': '10','FL': '12','GA': '13','HI': '15','ID': '16',
    'IL': '17','IN': '18','IA': '19','KS': '20','KY': '21','LA': '22',
    'ME': '23','MD': '24','MA': '25','MI': '26','MN': '27','MS': '28',
    'MO': '29','MT': '30','NE': '31','NV': '32','NH': '33','NJ': '34',
    'NM': '35','NY': '36','NC': '37','ND': '38','OH': '39','OK': '40',
    'OR': '41','PA': '42','RI': '44','SC': '45','SD': '46','TN': '47',
    'TX': '48','UT': '49','VT': '50','VA': '51','WA': '53','WV': '54',
    'WI': '55','WY': '56'
}


URL = "https://aqs.epa.gov/data/api/annualData/byState"
data = []

for pollutant, param_code in POLLUTANTS.items():
    for year in years:
        for state in states:
            code = state_to_codes[state]
            
            params = {
                "email": EMAIL,
                "key": API_KEY,
                "param": param_code,
                "bdate": f"{year}0101",
                "edate": f"{year}1231",
                "state": code
            }
            response = requests.get(URL, params = params)

            if response.status_code == 200:
                d = response.json().get("Data", [])
                data.extend(d)
            else:
                print("Failed for state {state} in {year} (Status {response.status_code})")
            
            time.sleep(1)

df_air = pd.DataFrame(data)
df_air.to_csv("raw/raw_air_quality.csv", index=False)


        
