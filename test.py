import multiprocessing as mp
import requests
print("Number of processors: ", mp.cpu_count())

import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[1000, 5])
data = arr.tolist()
data[:5]

# Parallelizing using Pool.map()
import multiprocessing as mp
# Redefine, with only 1 mandatory argument.
def howmany_within_range_rowonly(arg):
    r = requests.get(url)
    print(r)

url='http://35.189.233.152'
pool = mp.Pool(mp.cpu_count())
pool.map(howmany_within_range_rowonly, [row for row in data])
pool.close()
#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
