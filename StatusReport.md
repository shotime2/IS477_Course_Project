
Looking back on our timeline and plan for our group project in IS 477, we have made a lot of progress towards our final goal. Ultimately, we still want to use the same two datasets about Electric Vehicles and Air quality trends as our main focus is finding a relationship between the density of electric vehicle charging stations and improvements in air quality.

Updates: 

Everything done here was done on VSCode using Python

As for our project right now, our storage and organization contain multiple folders with files inside including raw, clean, merged, scripts, analysis, and docs. So far, the folders that are pushed to github are clean, merged, and scripts since we still need to complete the other folders. We also have a .gitignore file to ignore the raw folder since our raw datasets are too big and are greater than 100MB, so we ignore that folder when we push our commits to github. We also have a READMe.md file that is temporarily being used to explain why raw folder isn’t committed to github. In that file, we linked a Google Drive folder link where you can view both the raw datasets. Other files that are not in the main folders are the StatusReport.md and also a requirements.txt file where we plan to include all the required libraries, tools, and requirements to be able to reproduce our project.

In terms of data collection and acquisition, we placed all our raw data in the raw folder. For the EV Vehicle dataset, we just downloaded the csv from PlaceKey, but to get the Air quality data, we have a fetch_air_data.py file to fetch the raw data and place the csv output to the raw folder.

For the preprocessing and integration of our data, most of the work was done in the scripts. We have an ev_clean.py file in scripts that extracts 12 columns from our EV dataset, making sure fuel type = “ELEC”, and also only including data from 2014-2024. We also drop missing values from those columns and convert the date column to be include only the year so its prepared for grouping. We drop any duplicates and make sure the State column has valid states, by filtering out the Canadian states. We then groupby state and year using .size() to get the EV station count per state and year. This csv is outputted to the clean folder. To get our air quality data, we got our API key when we signed up with our email on EPA AQS website. We created fetch_air_data.py file where we standardized our data by mapping our states to their corresponding state codes and pollutants to pollutant codes. We send API requests for each pollutant, for every year from 2014-2024, across all EV-eligible states, and collect it into one csv dataset that is outputted to the clean folder. Our scripts folder also includes a air_data_clean.py file that filters for "state_code", "parameter", "arithmetic_mean", "year" columns. We check for missing state values and drop them and make sure that the parameter column has a valid pollutant. We also remove any row where state could not be mapped. After that we grouped by state, year, and, parameter and calculate the average pollutant for each group. However, the data was in long format so we used a pivot tablr to convert it into wide format so each pollutant had its own column. The final clean csv was then outputted to the clean folder. The last file in our scripts folder so far is our merge.py which reads in both of the cleaned datasets from the clean folder and merges them via state and year using an inner join. This merged dataset is outputted to the merged folder.

To begin our analysis of the merged datasets, we wanted to create a few different visualizations. The first one we worked on was a correlation matrix we built using the “ev_station_count” against the mean Carbon Monoxide, Ozone, and the PM2.5 levels in those respective states. To do so, we created a new file where we imported pandas. We then compared the correlations using the “.corr()” function and saved the matrix to a new file within our Analysis tab. 
Moving forward we wanted to create a scatterplot that would visualize the the actual levels of each of the pollutants. To do so, we imported “matplotlib.pyplot” as “plt.” For each gas in the atmosphere and in the air, we compared them to the number of electric vehicle chargers to show the correlation visually. 
At this point we have the correlation matrix, and one of the scatterplots that describes the Carbon Monoxide relationship. Moving forward we will build two more scatterplots for each of the other gasses. We will follow this up by analyzing what these graphs are describing, and use them as evidence to support the answers to our guiding questions.



Updated Timeline:

Timeline:  
9/26: Create a group repository and select Datasets (Shobhit)          Status:COMPLETE
10/16: Complete the Project Plan  (Shobhit and Carter)                                       Status: COMPLETE
10/30: Access the datasets and compare side by side (Shobhit)
Status: COMPLETE
11/19: Clean and Pre-Process the Datasets (Shobhit)
Status: COMPLETE
11/30: Find correlations and develop visuals (Graphs, charts) (Carter)
Status: IN PROGRESS
12/2: Analyze our findings based on evidence (Carter)
Status: IN PROGRESS
12/5: Finalize Interim Status Report(Carter)
Status: IN PROGRESS
12/8: Answer our initial questions and draft our final project (Shobhit & Carter)
Status: NOT DONE YET
12/9 : Finalize our project and revise for clarity and coherence (Shobhit & Carter)
Status: NOT DONE YET
12/10: Submit Project (Shobhit & Carter)
Status: NOT DONE YET

Based on our current progress, we updated our previous Project plan timeline to make sure the dates aligned with our current work. We changed the order for some of our tasks because some tasks took longer than expected.

Next Steps:
	Other smaller aspects of the project that we still need to complete include the docs folder, the requirements.txt, README.md, etc. The docs folder will contain the metadata and documentation of our datasets and our code. It will also most likely include our Workflow automation diagram. Our requirements.txt will include all the required libraries, tools, etc. to be able to reproduce our project. Our README.md will be a project report summarizing our title, contributors, data profile, data quality, findings, future work, reproducing, and references.
Overall, our original plan is holding together quite well. The datasets have not caused any serious problems that redirect our goals. We will continue to analyze the two datasets and establish if there is a correlation between charging stations and air quality, or if there are confounding variables. We will need to establish our correlations and visuals to defend those correlations, likely using scatterplots and correlation matrices. Visualization will help deliver evidence to further analyze why our outcome is what it will be. These analyses will go beyond the surface, and will describe the specific actions taken to find the evidence that supports it. This will all most likely go under the analysis folder of the project.
Our conclusions from analysis will then lead us to answering our initial questions stated earlier. These answers will indicate the finalization of our project. At this point all that will be left to do is to ensure that all of our findings and conclusions are clear, coherent, transparent, and most importantly replicable. By submitting our projects to Github, they will be publicly available for someone to replicate. This will give people the opportunity to take our work and dive deeper into more specific areas, or answer questions that might arise down the road.


Shobhit’s Contribution Summary:
For this milestone, I contributed by handling the preprocessing and integration of our data. I extracted our raw data from downloading EV csv and fetching from EQS API. I created scripts to clean each of the raw datasets by handling missing values, standardizing data, and grouping by state and year. After cleaning both datasets, I merged them both using an inner join.

Carter’s Contribution Summary:
Up to this point in the project I built off of the merged datasets to begin our visualizations. In Visual Studio Code I made a correlation matrix, and wrote the code for the three scatterplots. While we have the code, we need to be able to save the second two scatterplots going forward.

