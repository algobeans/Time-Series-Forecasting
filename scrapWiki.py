import json
import urllib2
import pandas as pd
from optparse import OptionParser

parser = OptionParser()
(options, args) = parser.parse_args()

d = list()
# for each year
for i in range(2008,2017):
    # for each month
    for j in range(01, 13):
        # get url
        url = "http://stats.grok.se/json/en/"+str(i)+str(j).zfill(2)+"/"+args[0]
        # extract json data
        dfull = json.load(urllib2.urlopen(url))
        dviews = dfull["daily_views"].items()
        # append data to main list
        d = d + dviews

# convert list of tuples to dataframe
df = pd.DataFrame(d, columns=['ds', 'y'])

# sort by date
df = df.sort_values(by='ds')

# remove invalid dates
df.ds = pd.to_datetime(df.ds, errors='coerce')
df = df.dropna()

# save as csv
filename = args[0]+".csv"
df.to_csv(filename, index=False)
