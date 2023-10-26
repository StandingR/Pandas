import pandas as pd
import numpy as np

s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
print(s[np.arange(1,4,2)])
