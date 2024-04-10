# NumPy RuntimeWarning: divide by zero encountered in log10

import numpy as np

arr = np.array([4, 12, 0, 16, 160, 320])

with np.errstate(divide='ignore'):
    print(np.log10(arr))