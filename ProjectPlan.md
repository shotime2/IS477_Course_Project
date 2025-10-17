Overview:  
The goal of this project is to find out if there is a relationship between the density of electric vehicle charging stations and improvements in air quality. Especially in a world where electric vehicles like Tesla are starting to become more popular, we would like to see if there is some relationship that could help decide in the future if switching the EV is more environmentally friendly in terms of air quality. Our findings could help inform city planners and policymakers about the benefits or harms of investing in more EV infrastructure in areas struggling with air pollutants.  We will be looking at data over a ten year period from 2014-2024 and focus on the most toxic air pollutants like PM2.5, Ozone, CO2, etc. The data will be combined from two different sources: EV Charging Stations dataset from the U.S. Department of Energy and Air Quality data from the EPA Air Quality System API. 
 
Research Questions: 
 
Our primary research question is this: 


Is there a relationship between EV Charging Station density and air quality improvements across U.S. states between 2014 and 2024? 
 
We also have some smaller questions that we might also answer depending on how long the primary research question takes or if we encounter some difficulties. However these could change: 
 
Are certain types of pollutants more strongly associated with an increase in EV infrastructure? 
Which states with the most EV infrastructure have the worst air quality? 
Is there a relationship between certain types of EV connectors and air quality? 
 
Team: 
 
Shobhit Venkataraman’s Role: Work on data collection, integration, cleaning, storage & Organization, Analysis, Extraction 
 
Carter Reid’s Role: Work on Analysis, Visualizations, Ethical data handling/ethics, Workflow automation, Metadata & documentation 
 
-We will work on the remaining tasks together 
 
Datasets: 
 
https://www.placekey.io/datasets/ev-charging-station  
The EV Charging Station Dataset contains data on electric vehicle charging stations located in the United States and Canada. The link to the public csv dataset was found at PlaceKey, but its a resource pulled from the U.S. Department of Energy’s Alternative Fuels Data Center. Some key fields in this dataset are station name, facility type, Access Code, latitude, longitude, State, city, county, ZIP, EV Network, Connector Types. This dataset will be used for measuring EV growth and density over time by grouping based on state and regions.


https://aqs.epa.gov/aqsweb/documents/data_api.html#annual
The Air quality data comes from the Environment Protection Agency’s Air Quality System API. To access the data, we will need to write API requests based on annual data and state since that is what our main research question requires: /annualData/byState. This dataset is public, but we will need a registered API key to download it as CSV or JSON. This dataset will contain annual summaries of air pollutant concentrations. Key fields are state, parameter code(pollutant), mean, max, percentiles, year, state, units, observation counts. This dataset combined with the EV charging station dataset will allow us to analyze air quality trends based on EV growth across U.S. states. 




Data Lifecycle/Ethical Data Handling:
Both datasets are publicly available. There is no personal identifiable information. Will have proper citation for all datasets and compliance with EPA API terms of use


Data Collection & Acquisition:
EV Charging Station Dataset is CSV downloaded from PlaceKey. Air quality data collected through repeated API requests to EPA AQS API.


Storage & Organization:
Raw datasets will be placed in a folder called raw while the processed and cleaned datasets will be placed in a folder called clean. There will be multiple files under each folder and we will use either relational SQL databases or pandas DataFrames to organize the data.


Extraction & Enrichment:
Only the key fields we stated in the Dataset section will be extracted like station name, facility type, Access Code, latitude, longitude, State, city, county, ZIP, EV Network, Connector Types, parameter code(pollutant), mean, max, percentiles, year, state, units, observation counts. These will all be standardized.


Data Integration, Quality, Cleaning: 
We will merge our datasets based on state, but we will adjust for the other smaller research questions. The pollutant means and EV charging station count will be aggregated based on region and year. We will handle missing values, remove duplicates, and make sure units are standardized. 


Workflow Automation and provenance:
Python scripts and/or SQL  will be used to automate data collection, cleaning, integration, and analysis. We might implement a main file for the end-to-end workflow or Snakemake workflow. Files will all have documentation to explain the code.


Reproducibility & Transparency:
We will make a requirements.txt file for instructions, things to install for Python, API key setup, and documentation for tech-stack. It will be detailed and easy to understand for reproducibility. 


Metadata & Data documentation:
We will include metadata files to describe our datasets including context for variables, units, and sources. Documentation will be spread throughout the project to explain what is going on.


Timeline:  
9/26: Create a group repository and select Datasets (Shobhit)
10/16: Complete the Project Plan  (Shobhit and Carter)
10/23: Access the datasets and compare side by side (Shobhit)
10/30: Clean and Pre-Process the Datasets (Shobhit)
11/6: Find correlations and develop visuals (Graphs, charts) (Carter)
11/13: Finalize Interim Status Report (Carter)
11/20: Analyze our findings based on evidence (Carter)
11/27: Answer our initial questions and draft our final project (Shobhit & Carter)
12/4 : Finalize our project and revise for clarity and coherence (Shobhit & Carter)
12/10: Submit Project (Shobhit & Carter)


Constraints: 

Some constraints we might face throughout this project relate to both the data set alignment and the resources within our team. As it refers to our data, the two sets could struggle with timing. For example, the air pollution data might be updated as regularly as day to day, whereas the electric vehicle chargers might be more static and will not change as regularly. Additionally, the air quality will fluctuate a lot depending on factors with the environment and weather, while the chargers will likely not be removed once they are installed. Another main concern is how Covid-19 could affect our analysis since we are looking at a ten year period from 2014-2024. We need to consider in our report that our results could be skewed around 2020 to 2022 since the lockdown would’ve improved air quality. Our constraints with our team will consist of finding times to meet during the week around our busy schedules. We will need to utilize our time efficiently and our individual skills to ensure we stay on our timeline.  
Other data-related constraints include the access restrictions that may be applied on these datasets. Using API keys could limit us to certain amounts of usage to collect data. Even after collecting it, the entire dataset could be so large depending on the update cycles. If there is data on the air quality from every day for ten to twenty years, there will be a lot of samples. This could lead to slow running times if most of the data qualifies for our research. Looking forward to the rest of the semester, we will be constrained by the amount of knowledge we have and when we learn each additional skill. Some examples we might want to incorporate are descriptive, predictive, and prescriptive analyses. These will be solved as we progress through the course and continue to develop these skills. 


Gaps: 

Some gaps that exist in our research before we begin are: 
What size of areas will we compare? (state, zip code, city) 
Should we compare economic data, or other demographic information on the area that we apply this data to? 
What are the confounding variables related to each dataset that we should consider removing before we analyze? 
Should we consider the types of pollutants in the air when determining what the chargers helped reduce? 
Should we gauge certain chargers’ usage amounts to ensure that the relationship we find actually exists? 
How should we eliminate intrinsic biases to ensure that our research is not influenced by previous notions? 


Most of these questions will be answered before we begin dissecting the datasets; however, some of them might be delayed until we run into them during the project. These gaps will not cause problems within our research as they are simply questions we need to answer in order to have truthful, consistent hypotheses.  


