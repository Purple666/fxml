"""Plot fxdata that was formatted in format_fxdata.py"""

import numpy as np
import matplotlib.pyplot as plt
import h5py

# User input
# Default output filepath and name in scrape_forexite.py
fipath = 'C:/gh/data/fx/format/'
finame = fipath + '2010_01.hdf5'

# Import data
with h5py.File(finame, 'r') as fi:
    opens = fi['opens'][:]
    dates_tstart = fi['dates_tstart'][:]
    dates_tend = fi['dates_tend'][:]
    dates = fi['dates'][:]

# Format dates to readable strings
dates = dates.astype(np.int)
dates_str = np.zeros(len(dates), dtype=object)
for d in range(len(dates)):
    dates_str[d] = str(dates[d, 0]) + '-' + \
        str(dates[d, 1]) + '-' + str(dates[d, 2])

# Plot EUR/USD
EURUSD_idx = 0
t = np.arange(dates_tend[-1])
plt.figure()
plt.plot(t, opens[EURUSD_idx, :])
plt.xticks(dates_tstart, dates_str)
plt.xlabel('Date')
plt.ylabel('EURUSD')
