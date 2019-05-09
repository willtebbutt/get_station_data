import numpy as np
import pandas as pd
from get_station_data import ghcnm


### Specify station information to load.
data_version = 'v3.3.0.20190411'
data_fname   = 'ghcn_monthly_temperature/ghcnm.v3.3.0.20190411/ghcnm.tavg.'+data_version+'.qca.dat'
stn_md_fname = 'ghcn_monthly_temperature/ghcnm.v3.3.0.20190411/ghcnm.tavg.'+data_version+'.qca.inv'

stn_md = ghcnm.get_stn_metadata(stn_md_fname)

stn_md.head()


### Specify stations to analyse

country_names = ['ANTARCTICA']

my_stns = ghcnm.extract_countries(stn_md, country_names)

my_stns.head()


### Extract data for specified stations into a Pandas DataFrame
df = ghcnm.get_data(data_fname, my_stns)
df.tail(n=10)


df.drop(columns=['dmflag', 'qcflag', 'dsflag']).tail(n=10)

### Save to file
df.to_csv('Egypt_surrounding_ghcnm.csv', index=False)

# Questions:
# How many stations do I actually have?
# How does this chime with what I actually want to do?



# Select stations based on lat and lon.
df = stn_md

europe_df = df[(df.lat > 36) & (df.lat < 72) & (df.lon > -11.2) & (df.lon < 34)]
europe_df.to_csv('european_stations.csv', index=False)

df.to_csv('global_stations.csv', index=False)


