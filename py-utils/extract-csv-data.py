# Bandbreitmessung mit der BBM App der Bundesnetzagentur
# Data extracted for E-Mail an provider

import pandas as pd
import re

# List that stores the obtained percentage of promised bandwidth
scans_percentage_received = []

# Read the whole file
df = pd.read_csv("/path/to/Breitbandmessung.csv")
print(df)


# Extract relevant infos:
df = df[[' Download Soll', ' Download Ist',
          ' Verhältnis', ' Upload Soll', ' Upload Ist', ' Verhältnis']]
print(df)




# Testing with a result at column 'Download Ist' row 7 
# Extracting only the float number for analyse.

result = df.at[7, ' Download Ist']
just_speed = result.split(' ')
result = just_speed[1]

if float(result) < 50.0:
    print('You get less then 10% of the promissed bandwidth!')
    bandwidth_percent = float(result) / 500 * 100
    scans_percentage_received.append(bandwidth_percent)
else:
    print('You get more than 10%')

print('List of the % of your Bandwidth that you receive: ','\n',scans_percentage_received)