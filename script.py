import pandas as pd
from sodapy import Socrata
import os  # also need os
from dotenv import load_dotenv

load_dotenv()  # blank if .env file in same directory as script
# load_dotenv('<path to file>.env') to point to another location
APPTOKEN = os.getenv('APPTOKEN')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# # Unauthenticated client only works with public data sets. Note 'None'
# # in place of application token, and no username or password:
# client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cityofnewyork.us",
                 APPTOKEN,
                 username=USERNAME,
                 password=PASSWORD)

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# Motor Vehicle Collisions - Crashes DB from NYC open data
count = client.get(
    "h9gi-nx95", 
    select="count(collision_id)",
    where="crash_date > '2014-10-28T00:00:00.000' AND number_of_persons_killed is not null AND number_of_persons_killed > 0",
)
print(count)
print(int(count[0]['count_collision_id']) / (8 * 365))

records = client.get(
    "h9gi-nx95", 
    limit=100,
    select="crash_date,crash_time,latitude,longitude,number_of_persons_injured,number_of_persons_killed",
    where="crash_date > '2014-10-13T00:00:00.000' AND number_of_persons_killed is not null",
    order="number_of_persons_killed DESC, number_of_persons_injured DESC, crash_date DESC, crash_time DESC"
)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(records)
print(df)

# TODO find the relationship between crash_time and crashes
# TODO find the relationship between latitude, longitude and crashes 