import numpy as np
import pandas as pd
from get_station_data import ghcnm


### Specify station information to load.
data_version = 'v3.3.0.20190508'
target_dir = 'ghcnm.' + data_version + '/ghcnm.tavg.'
data_fname   = target_dir + data_version + '.qca.dat'
stn_md_fname = target_dir + data_version + '.qca.inv'

stn_md = ghcnm.get_stn_metadata(stn_md_fname)
all_names = np.unique(stn_md['country']).tolist()
all_stns = ghcnm.extract_countries(stn_md, all_names)

data = ghcnm.get_data(data_fname, all_stns)

data_prime = data[['lat', 'lon', 'elev', 'month', 'value']].dropna()
data_prime.to_csv('global_station_data.csv', index=False)


def get_data_in_rect(df, lat_lb, lat_ub, lon_lb, lon_ub):
    return df[(df.lat > lat_lb) & (df.lat < lat_ub) & (df.lon > lon_lb) & (df.lon < lon_ub)]

# Select stations based on lat and lon.
df = stn_md # change this to data

europe_df = get_data_in_rect(df, 36, 72, -11.2, 34)
europe_df.to_csv('european_stations.csv', index=False)

df.to_csv('global_stations.csv', index=False)

# Construct dictionary for station df access.
stn_dict = dict([(row['station'], n) for (n, row) in all_stns.iterrows()])
