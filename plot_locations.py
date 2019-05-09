import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np


# Load the data and pull out the unique lats and lons.
# Columns are lat, lon, elevation, month_of_year, T
data = np.genfromtxt('global_station_data.csv', delimiter=',', skip_header=1)

latlon = data[:, 0:2]
unique_latlon = np.unique(latlon, axis=0)
lats, lons = unique_latlon[:, 0], unique_latlon[:, 1]

ax = plt.axes(projection=ccrs.PlateCarree())
ax.scatter(lons, lats; s=0.2, alpha=1)
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=":")
ax.add_feature(cfeature.LAND)
ax.set_extent([-180, 180, -90, 90])
plt.show()
