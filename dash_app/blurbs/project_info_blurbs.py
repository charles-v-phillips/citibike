project_blurb = '''This project investigates Citi Bike, the exclusive bike share provider for New York City. Bike sharing is a peer-to-peer consumer business model to address the traditional last-mile problem in public transportation. In metropolitan areas, commuters are often stuck with the decision between a lack of public transportation (either subway or buses) to reach the target destination or suffer in the traffic jam, lack of parking spaces, and the air pollution if they choose to drive private vehicles. Bike sharing makes public transportation more attractive by offering the 'last-mile' transportation equipment (through timed rental) from the transportation hubs to/near the target destination.

Citi Bike operates 24 hours a day, 7 days a week, and 365 days per year. As of this writing, Citi Bike has 23,472 bikes and 1,493 docks within their system.  There are approximately 96,420 rides per day, with each bike being used on average 4.37 times per day. Citi Bike is operated by Motivate, a subsidiary company of Lyft. Citi Bike gained a monopoly to operate shared-bikes in NYC (granted by NYC DOT) expiring in 2029. The lack of competition allows it to open up the per-ride data in exchange for faster innovation. This allows us to use its data for our case study. The total revenue for the month of October 2021 was $7,513,934.59 with $5,885,385.13 from membership and user fees and $258,380.55 from sponsorship.

A major issue with the Citi Bike bike share model is the imbalance of bike availability based on user usage patterns. Similar usage patterns amongst riders will result in stations with either a surplus or deficit of bikes, dependent on location and time of day. The system is not self-sustaining and requires intervention from operators to serve all customers. If a dock is empty and a user wants to rent a bike, that user will be turned away. Likewise, if a dock is full near a customer's destination the user will not be able to park the bike in their chosen location.

The goal of this project is to provide insights into Citi Bike’s operation and provide recommendations to rebalance the bike system to increase customer satisfaction and retention.

'''

data_blurb = '''The ride data is hosted by Citi Bike. From June 2013 - January 2021, there are ~114 Million Observations. Public data was reformatted starting in February 2021 and was excluded from this analysis. The features of this dataset includes bike id, start location, end location, trip duration, start time, end time, and user type.

The dock availability information is hosted by TheOpenBus. The dock availability data ranges from March 2015 to April 2019 and has ~35 Million Observations. Features include dock id, dock name, date number of available docks,  and total docks.

The weather data was incorporated when modeling, and retrieved from NOAA. The only features that were used from that dataset were the rain and temperature. All historical data within the date scope is included, in addition to weather projections for 48 hours into the future.

The rebalancing Rides Data was inferred from the Citi Bike rides dataset, and was ~4.7 Million Rows. These rides were interpolated from rides that had an end station that did not match the start station of the next ride from the same bike ID.
'''
