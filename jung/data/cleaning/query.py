import google.cloud
client = google.cloud.bigquery.Client()
query = """
SELECT DISTINCT start_station_name FROM `citi-bike-333915.citi_bike_data.full` ORDER BY start_station_name ASC
"""
query_job = client.query(query)

for r in query_job:
	print(r)