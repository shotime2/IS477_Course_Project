Due to Github's 100MB file size limit, our raw datasets are stored in Google Drive:

https://drive.google.com/drive/folders/1XSjTFuxP7Xa8inqFg8wl0O0j4pRysx6n?usp=sharing


Title:
EV Charging Station Growth and its Relationship with Air Quality Across U.S. States (2014- 2023)

Contributors:
Shobhit Venkataraman
Carter Reid

Summary:

In today’s word, Electric vehicle companies like Tesla and Rivian are becoming more popular for daily commuters and many other car companies are shifting their focus to developing their own EVs. With the rise in EVs in the United States, it would beg the question whether the environment’s air quality would improve. This is because we assume that switching from gas-powered cars to EVs would reduce emissions, and thereby improving overall air quality. Gas-powered vehicles contribute heavily to pollutants like Carbon monoxide, ozone precursors, nitrogen oxides, and particulate matter while EVs produce no tailpipe emissions. However, air quality can be influenced by many different factors including natural disasters, industrial emissions, weather, agriculture, etc. Also EV density varies across states due to population and economy so this raises the question to what extent do these two correlate.

Our motivation for doing this project comes from this assumption and we wanted to find out if there is a relationship between the density of electric vehicle charging stations and the improvement of air quality. We believe that our findings could help inform city planners and policymakers about the benefits or harms of investing in more EV infrastructure in areas struggling with air pollutants.  We will be looking at data over a time period from 2014-2023 and focus on the most toxic air pollutants like PM2.5, Ozone, and CO.

Research Question:
Is there a relationship between EV Charging Station density and air quality improvements across U.S. states between 2014 and 2023?


To answer our research question, we acquired and integrated two datasets.


1. EV Charging Station Dataset: This dataset contains data on electric vehicle charging station located in the United States and Canada. This is a public csv dataset found on PlaceKey website, but its a resource pulled from the U.S. Department of Energy’s Alternative Fuels Data Center. We cleaned and preprocessed the raw data, filtering for “ELEC” fuel type, removing non U.S. observations, standardizing columns, and converting date values to year. After we grouped the stations by state and year to measure EV charging station density growth.


2. EPA AIr Quality System Dataset: This dataset comes from the U.S. Environmental Protection Agency’s AQS API, which gives annual air pollutant data for Pm2.5, Carbon Monoxide, and Ozone at the state level. It is not directly downloadable so we had to authenticate using an API key and a specific endpoint; we called /annualData/byState endpoint for each pollutant across all states from 2014 to 2023. We standardized our API requests by mapping the states to their state codes and the pollutants to their pollutant parameter code, and then automated it for every year in our range. We normalized them into tabular form, filtered for valid codes, converted to annual averages, and also pivoted it into a wide table so each pollutant had its column.


 It seemed that the data we retrieved from AQS only went from 2014 to 2023 and there wasn’t any 2024 data. This was the reason for making our range from 2014 to 2023 instead of the original ten year analysis from 2014 to 2024. We also found that Carbon monoxide barely had any observations compared to Pm2.5 and Ozone. When we tried making scatterplots for each of the pollutants later in the project, the Carbon monoxide graph didn’t have any valuable information so we decided to only focus on the other two pollutants in the analysis. After merging our cleaned EV and air quality datasets using an inner join on state and year, we found that we were missing some of the states. This was because AQS API didn’t have pollutant data on some of the states like CA, AL, CT, etc and we ended up with around 43 states after the merge.


In our analysis, we computed the changes in pollutant averages and EV growth, built a correlation table, and created scatterplots for each pollutant to identify any patterns. Our results showed mostly weak correlations between EV charging station growth and pollutant changes for both pollutants. Some states with EV growth showed some PM 2.5 improvements, but some also showed increase. Ozone’s relationship looked even weaker as the changes were in the thousandths. They were really small as most of the states clustered around 0, regardless of the EV growth. Overall, our findings suggested that EV charging station density doesn’t independently explain the trend with air quality from 2014 to 2023 in U.S. states. It may have helped improve air quality in some areas, but there are other factors like climate, industrial emissions, geography, fires, population, etc that could also explain these results. 




Data Profile:

The project focuses on two data sources to find a relationship between electric vehicle infrastructure growth and changes in the air quality across U.S. states. Our first dataset is EV Charging Station Dataset from PlaceKey and our second dataset was retrieved through requests to the U.S. Environmental Protection Agency’s Air Quality System API.


The EV Charging Station dataset is a comprehensive resource providing detailed information of Elecrtic Vehicle Charging stations across the United States and Canada. The dataset is originally from the Alternative Fuels Data Center which is federally maintained by the U.S. Department of Energy’s Vehicle Technologies Office. The AFDC was established in 1991 in response to the Alternative Motor Fuels Act of 1988 and the Clean Air Act Amendments of 1990 to help support policymakers, city planners, etc. The dataset was established to support the adoption of alternative fuel vehicles and serve as a valuable tool for electric vehicle owners and planners in expansion, route planning, and charging needs. 
This dataset includes tens of thousands of records across North America and there are 75 columns in total. The most valuable columns to our study are 'ID', 'Latitude', 'Country', 'ZIP', 'Longitude', 'Station Name', 'EV Connector Types', 'Open Date', 'City', 'EV Network', 'State', and  'Fuel Type Code'. Since the EV transition is evolving rapidly, the AFDC sporadically updates records in this dataset. In terms of legal considerations, the EV Charging Station dataset is publicly licensed and the AFDC supports open access for planning and research rather than unrestricted redistribution. There are also possible ethical considerations like personal information including phone number and Owner Type Code, which could be misused. Another concern would be a policy attribution problem due to the fact that this dataset includes both U.S. and Canadian data, since both U.S. EV infrastructure and Canadian infrastructure operate under different energy regulations. There are also fields like update timestamps and access restrictions which could possible lead to security vulnerabilities. Overall, the dataset is ethically valid because data is mostly about the station data rather than actual individuals.


The Air quality dataset was retrieved from the U.S. Environmental Protection Agency’s AQS API. This dataset is not downloadable like the EV dataset and instead users need to register with an email to get an API key. The AQS is a federal repository that is collected by state, local, tribal, and federal air pollution control agencies from thousands of monitors across the nation.It requires structured requests that include variables like email, key, param, bdate, edate, and state. There are many types of services including monitors, lists, daily summary, quarterly summary,etc., but we chose annual summary because our analysis is based on yearly trends. In terms of legal constraints, this dataset is also publicly accessible with subject to responsible handling. In terms of ethical concerns, this data we requested doesn’t really have privacy concerns since our variables are not personal identifiers. However, the API includes request limits and terms of service that should be followed. All services should have the end date and begin date in the same year with a maximum of five parameter codes in a single request. They also ask to please limit size and frequency of queries since their system can only process a limited amount and its possible for your account to be disabled. 


Data Quality:


We made sure to evaluate both of our datasets quality across Accuracy, Completeness, Consistency, and Timeliness. We judged our datasets for accuracy based on how well our data reflects the values it intends to measure. For our datasets, accuracy depends on how well the data reflects real-world values it is trying to measure.  The EV dataset’s accuracy depends on the U.S. Department of Energy’s Alternative Fuels Data Center’s reporting process. The data is all federally managed so the data should be completely accurate, but some fields depend on self-reporting from the stations which could be inaccurate. Most of the variables are hard to verify like when Date was last confirmed, EV Network, Status code, etc, and even the EV pricing which is subject to change based on time of day. However, we checked for unique identifiers to make sure that all the ID records were unique and they were. We also conducted logical checks for impossible values in variables like Open date to make sure the years were valid and not in the future. Similarly, the EPA AQS dataset comes from air pollution control agencies and their regulated monitors, meaning it should strong in terms of accuracy. The only concern would be that heavily monitored states would probably provide more accurate averages compared to less monitored states. We made sure to verify that all state codes and years were valid. Overall, both datasets are accurate.


In terms of completeness, the EV dataset is missing a lot of information. There are around 35 columns that are basically completely empty with some having an exception of a few records out of the thousands. These columns are extra columns including Hydrogen Status Link, NG Vehicle Class, NPS unit Name, CNG Storage capacity, etc. We didn’t use them since they had no impact on our analysis, but that is around half of all columns missing the majority of its data, which is really concerning. There are still columns including Cards Accepted and Facility Type that are also missing large amounts of data, but not as much as the others. The AQS API also had completeness issues since some states had no valid pollutant readings for our time range, so we missed out on important averages from major EV states like California. This also caused our merged dataset to have around 43 states rather than all 50, so we lost the EV data for those states. After cleaning this dataset, we found that Carbon monoxide had many observations missing while the other two pollutants were not missing any. This forced us to exclude Carbon monoxide from our analysis later on. Overall, the completeness for both the datasets are concerning.


To evaluate timeliness for our dataset, we were concerned with how current the data is and what are the update frequencies. For the EV dataset, it is updated sporadically and the data is pretty recent. Majority of the data in Open Date seemed to be post-2014, which is great since that is the starting year for our analysis. Even for the Updated At and Date Last Confirmed columns, majority of the data is from 2023 and 2024, which is very recent and aligns with our end year in our analysis. The EPA AQS dataset states that the annual aggregates may appear 6 months or more after collection, so the data from 2025 is not in the dataset yet. This is fine for our analysis since our ending year is 2023. Overall, the timeliness is not concerning.


For consistency, we made sure to evaluate whether our datasets formats are consistent. In the EV dataset, some fields contained different versions of the same data type. For example, the Latitude and Longitude columns had data where some had more decimals than others. Some data points in Latitude were formatted like 44.1413124983078 and some had less decimals like 37.442587. Some columns had data that were in complete different formats. For example, the ZIP column contained the ZIP code of the station location and some were formatted in all numbers like 92252 and some were formatted in a mix of numbers and letters like “M4W 1A5”. There were columns that had data that were mostly lowercase and data that were all uppercase. For example, the Station Name column had data like “Fairfield Inn & Suites” while other data were like “CAISSON RE WESTPARK PLAZA”. The AQS raw dataset was very consistent, but it required us to map tables for states and their state codes for the merge. Overall, the consistency is somewhat concerning.





Findings:


As mentioned before, our analysis consisted of a correlation matrix, and two scatterplots comparing the density of electric vehicle chargers and how they related to mean levels of pollutants by state. These three visualizations provided us with a solid baseline for determining the relationship between the important variables. 


<img width="641" height="179" alt="Screenshot 2025-12-09 at 10 24 04 PM" src="https://github.com/user-attachments/assets/3340fd36-284d-485e-9b86-3da2e2b2e8f8" />


Above is exhibit 1, a correlation matrix between the number of electric vehicle chargers in each state compared to the measurement of Ozone, and PM2.5 - Local Conditions which are two of the more prevalent greenhouse gasses emitted from gas powered vehicles. As you are aware, the higher a correlation, the more linearly related the two variables are. Given that the correlation coefficient between electric vehicle chargers growing in density and PM2.5 levels is only 0.20, many understandings can be made. First of all, it indicates that there is no linear relationship between the two variables because the coefficient is so low. Based on our research question, this leads us to believe that the number of charging stations does not contribute to the change in gas levels and air quality. Specifically, there is no relationship between the chargers and the levels of PM2.5. Although they are not supposed to reduce the levels of the gases in the air, it was assumed that the change would be minimized for more chargers in the area. Next, looking at the correlation coefficient between the chargers and the ozone levels is a –0.068. This implies that there is no correlation between the two. The negative amount is likely noise and cannot describe anything because it is so small. 



<img width="611" height="436" alt="Screenshot 2025-12-09 at 10 24 46 PM" src="https://github.com/user-attachments/assets/af98d67f-eae7-4032-a68c-5136df3a55ba" />



Next is the scatterplot developed to illustrate the relationship between electric vehicle chargers and the levels of PM2.5 - Local Conditions in the respective areas. These plots were designed to express the evolution of these numbers, and to show how it has changed since the introduction of so many electric charging stations. As you can see the relationship between chargers and PM2.5 as described in this graph is still little to no correlation. States like Massachusetts and Texas show high EV growth, but display pretty unique differences in PM2.5 changes. We can see that the majority of the states are below the 0 meaning the pollutant decreased, but most of those states are clustered in areas of low EV growth. The plot points are all scattered, but there looks to be a very slight upwards trend. However, it is clear that it is still very weak and not impactful. Like the weak positive correlation coefficient collected on our matrix, the more electric vehicle chargers there are does not imply there will be less increase in PM2.5 gas in the air.




<img width="663" height="428" alt="Screenshot 2025-12-09 at 10 25 22 PM" src="https://github.com/user-attachments/assets/2f0c8c5b-0a09-466b-8f4c-a34768155002" />



Following is the scatterplot made to highlight the effect the charging stations had on the levels of Ozone in their respective areas. This relationship can be used to evaluate if and how the charging stations impacted the Ozone in the air. The more Ozone in the air, the lower the air quality would be. Looking at the scatterplot, we can see that the Ozone levels do not change at an increased rate as the number of electrical vehicle charging stations increased. This would indicate that there is not indication of a linear relationship between them. Compared to the Pm2.5 scatterplot, the states are more clustered together, but the points on the graph are obviously not following any trend still. Outliers seem to be more prominent in this graph as seen with Utah. Relating to our research question, we conclude that the electric vehicle charging stations do not correlate with the Ozone levels whatsoever.  
Looking at all three of these visualizations, it is clear that there is no relationship between electric vehicle charging stations and the levels of certain gases in the air. None of these visualizations point to a linear relationship between the variables. In fact, they agree with each other that the charging stations do not impact the air quality at all. While this may change in the future, there is no substantial evidence to suggest that they do up to this point. 

Future Work:

Looking back over the course of this project, there were multiple lessons learned. Working with these datasets while learning concepts discussed in IS 477, we have developed a skillset that can be used in handling data going forward. Ideally, this project could be continued by anyone who is curious about these relationships and might want to take it further. The lessons focused on data quality and cleaning methods and choosing the right analysis methods for the given solution.  
The first lesson learned is related to the difference between correlation and causation. From an original perspective it might seem obvious that the increase of electric vehicles would lead to less gases emitted. While it might make sense that more electric vehicle chargers were a result of more electric vehicles on the road. If there were more electric vehicles, then they likely would replace the gas using cars. If there are less gas cars on the road and used it is safe to assume that there would be less gases like Ozone and PM2.5. Unfortunately, after looking at the results of our analysis, the measurement of these gases has little to no relation to the chargers. It is obvious that because something makes semantic sense, it definitely does not mean that there is an actual connection between things.  
The second lesson learned from this project is the importance of data quality. The higher quality the data you choose, the less work is needed to prepare it for analysis. Considering accuracy, a dataset in which the input data is entered consistently by the same person allows minimal syntactic errors. The clean consistent data within the datasets let the clean stay limited to dropping missing values. It was unnecessary to change specific words within the variables. Additionally, when the same person enters the data repeatedly, they will follow the same semantic rules every time. Assuming that the information they are inputting is true and relevant, the data will remain accurate throughout the entries. This makes projects like this much easier when dissecting datasets. 
Looking into the future, there are many ways people can proceed with this dataset. Some of the most likely and realistic examples are comparing this dataset to the number of electric vehicles sold each year. With the sales of electric vehicles, they could look to expand upon the project. They can look deeper at whether there is a relationship between cars sold and air quality. They can also note the impact of those cars being sold. If there is a linear relationship between the sale of cars and the charging station density, then it might begin to explain better how it does impact air quality. It would be useful to then use more of the air quality dataset and look deeper at the areas that have Carbon Monoxide levels. By singling out these areas, it might also help illustrate an underlying cause of the changes in air quality and rates that these pollutant levels increase. 


Reproducing:


First, go on our project’s github page and click the green “Code” button to copy the URL.  Then in an IDE like Visual Studio Code, clone the repository from the URL:


git clone https://github.com/<your-repo-name>/IS477_Course_Project.git


Navigate to the IS477_Course_Project folder:


cd IS477_Course_Project




In the terminal, create and activate a Virtual environment by writing this:
	
python3 -m venv venv


For Mac/Linux:
source venv/bin/activate


For Windows:
venv\Scripts\activate   


Download all required packages in requirements.txt:


pip install -r requirements.txt




We cannot publish the raw data to GitHub due to size and licensing restrictions, so here are instructions to retrieve it manually:


Download EV Charging Station Dataset from Placekey. Scroll down and click Download button next to “Interested in Full Dataset”: https://www.placekey.io/datasets/ev-charging-station
Save the csv in raw folder as ev_raw.csv


To retrieve Air quality data from EPA AQS API, go to this link: https://aqs.epa.gov/aqsweb/documents/data_api.html#annual 
Click on Sign up, to register with your email to get an API key. You will get the key in your email inbox. Then go to fetch_air_data.py in the scripts folder and replace the EMAIL and API_KEY with yours. Then run python scripts/fetch_air_data.py in the terminal.


      
Validate downloaded data by running this in the terminal. Compare with values in check_integrity.md
python scripts/check_integrity.py
 
Once data is present in the raw folder, you can automate our analysis by using Snakemake. In the terminal run:


snakemake –cores 1


This will automatically make the outputs in analysis folder and the merged dataset in merged. You can review the outputs and inspect the other files. 


Snakemake Workflow Diagram:

<img width="594" height="586" alt="Screenshot 2025-12-09 at 10 26 50 PM" src="https://github.com/user-attachments/assets/b56b670a-f00f-4ea0-9bf1-6275b5c57f1c" />


References:


1. GitHub 
GitHub. (n.d.). GitHub: Where the world builds software. https://github.com/ 
 
2. Visual Studio Code 
Microsoft. (n.d.). Visual Studio Code. https://code.visualstudio.com/ 
 
3. EPA Air Quality System (AQS) API 
U.S. Environmental Protection Agency. (n.d.). Air Quality System (AQS) API documentation: Annual data. https://aqs.epa.gov/aqsweb/documents/data_api.html#annual 
 
4. Placekey EV Charging Station Dataset 
Placekey. (n.d.). EV charging station dataset. https://www.placekey.io/datasets/ev-charging-station 




