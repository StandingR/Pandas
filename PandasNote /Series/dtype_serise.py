import pandas as pd
import numpy as np


arr = np.arange(100,105)

s = pd.Series(arr, dtype='int32')
print(s)