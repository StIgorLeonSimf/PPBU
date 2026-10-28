import numpy as np
import pandas as pd


nums = [[10, 20 ,30], [11, 22 ,33]]
print(nums * 2)
arr = np.array(nums)
print(arr.shape)
print(arr * 2)

d = {'price': [10, 20, 30], 'percent': [100, 200, 300]}
df = pd.DataFrame(d)
print(df)