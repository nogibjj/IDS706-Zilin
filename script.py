import pandas as pd
from sodapy import Socrata
import os  # also need os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
# import termplotlib as tpl

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
    select="crash_date,crash_time,latitude,longitude,number_of_persons_injured,number_of_persons_killed",
    where="crash_date > '2014-10-13T00:00:00.000' AND number_of_persons_killed is not null AND latitude > 40 AND longitude > -75",
    order="number_of_persons_killed DESC, number_of_persons_injured DESC, crash_date DESC, crash_time DESC"
)

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(records)
print(df.head)
print(df.dtypes)

df['crash_date'] = pd.to_datetime(df['crash_date'])
df['crash_time'] = pd.to_datetime(df['crash_time'], format='%H:%M')
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)
df['number_of_persons_injured'] = df['number_of_persons_injured'].astype(int)
df['number_of_persons_killed'] = df['number_of_persons_killed'].astype(int)

print(df.dtypes)

# find the relationship between crash_date and crashes
x = df['crash_date']
y = df['number_of_persons_killed']
# plotting 
plt.plot(x, y, 'bo')
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("date_crashes.png")
plt.close()

nx = df['latitude']
ny = df['longitude']
nc = df['number_of_persons_killed']
plt.scatter(nx, ny, s=10, c=nc, cmap='gray')
plt.savefig("location_crashes.png")