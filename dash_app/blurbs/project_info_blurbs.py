from dash import dcc
project_blurb = dcc.Markdown('''
Citi Bike is the exclusive bike share provider for New York City. 
Bike sharing attempts to fill in the gaps of traditional public transportation methods like subways and buses. 
This makes public transportation more attractive by offering the 'last-mile' transportation equipment from the transportation hubs to and from the target destination. 

Citi Bike operates 24/7 and has 23,472 bikes and 1,493 docks. 
There are approximately 96,420 rides per day, with each bike being used on average 4.37 times per day. 
The total revenue for the month of October 2021 was $7.5M, with $5.8M from membership fees. 
Citi Bike gained a monopoly to operate shared-bikes in NYC (granted by NYC DOT) expiring in 2029 in exchange for making their per-ride data publicly available. 

A major issue with the Citi Bike bike sharing system is the imbalance of bike availability based on usage patterns. 
Similar usage patterns amongst riders results in stations with either a surplus or deficit of bikes, dependent on location and time of day. 
The system is not self-sustaining and requires intervention from operators to serve all customers. If a dock is empty, the user cannot rent a bike and likewise, if a dock is full, the user cannot park the bike. 
The main goal of this project is to provide insights into Citi Bike’s current rebalancing strategy and offer a solution to further optimize these operations.


''')

data_blurb = dcc.Markdown('''
The ride data is hosted by Citi Bike, which contains ~114M rides from June 2013 - January 2021. 
Starting in February 2021, important features were no longer recorded so this data was excluded from the analysis. 
The features of this dataset includes bike id, start location, end location, trip duration, start time, end time, and user type.

The dock availability information is hosted by TheOpenBus, which contains ~35M rows from March 2015 - April 2019, after which the data was no longer publicly available. 
The features include dock id, dock name, date, number of available docks, and total docks.

Weather data (temperature and rain) was retrieved from NOAA, using all historical data within the date scope of the dock availability dataset.

The rebalanced rides data was inferred from the Citi Bike rides dataset and has ~4.7M rides. 
A rebalanced ride is defined as a ride where the previous end station ID did not match the next start station ID for an individual bike ID. 
This implies the bike was moved by a Citi Bike employee and was not recorded in the Citi Bike rides dataset.

''')


