from dash import dcc
rollout_clusters_blurb = dcc.Markdown( '''
Based on Citi Bike’s expansion plan there were 3 official dock rollout phases.
The figure shows the dock rollout by year from 2013-2021.
In 2013, stations were placed in Midtown Manhattan, Downtown Manhattan, and Downtown Brooklyn.
In 2015, expansion continued to Uptown Manhattan, continued to disperse around Downtown Brooklyn, and the first Queens stations were installed in Long Island City.
In 2017, Manhattan docks spread further uptown to Harlem and the Brooklyn and Queens docks continued to expand further away from Downtown Brooklyn and Long Island City, respectively.
In 2020, the dock network extended into the Bronx and continued the geographic spread of Brooklyn and Queens.
'''
)
pop_density_blurb = '''To better understand Citi Bike’s choice of the initial rollout, we investigated the Population Density of NYC. This information was taken from the New York Master Plan from 2021 available on NYC Open Data. We assumed the population density stayed relatively consistent over the time period from 2013-2021. From the map, we see that downtown Manhattan is quite populated, and so is downtown Brooklyn. This is a likely driving force for the locations chosen in the initial rollout phases.'''

transit_location_blurb = '''Based on the motivation of bikeshare to solve the ‘last mile’ of transportation, Citi Bike likely prioritized dock locations in the vicinity of public transit hubs. The figure shows dock locations plotted with subway stations and bus stops. In nearly all cases there is a dock within 1 block of each subway station and bus stop.'''

usage_plot_blurb = '''To better understand the usage patterns of Citi Bike customers, the number of rides per day and per hour were analyzed. During the weekdays, the most popular times were during the morning and afternoon rush hours. Significantly different usage patterns are observed for the weekends, where most rides occur during the afternoon.'''

ride_per_minute_blurb = '''This histogram displays the distribution of ride duration to the nearest minute. The peak of this distribution is at a ride duration of 6 minutes. The majority of rides last less than 15 minutes, likely used for commuting and connecting to subways and buses.'''

rides_per_month_blurb = '''The plot shows the monthly total number of rides every year. There’s a clear upward trend of total rides per year as well as a seasonal trend. The usership of Citi Bike took a hit when Covid-19 broke out, but the number of rides reached normal levels in the summer and fall of 2020.'''

rides_per_year_blurb = '''The total rides were plotted for each year from 2013-2020. There is a clear upward trend in the number of rides, with a slight dip in 2020, likely due to the onset of the Covid-19 pandemic.'''

rides_per_day_blurb = '''The plot shows rides per day from 2013-2021. The same seasonal trend can be seen from the Rides per Month plot. In the early years of operation a more clear daily trend over time can be seen with a ‘fanning out’ of points in later years. The additional variance in usage appears to correspond with the expansion of the system and incorporation of additional dock station location and additional usership.'''

eda_intro_blurb = '''In order to provide a solution to further optimize Citi Bike’s current rebalancing strategy, we first analyze trends in usage patterns.'''
