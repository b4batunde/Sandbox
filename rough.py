import numpy as np
import pandas as pd



nums = np.random.default_rng(2022)
arr = nums.normal(50, 10, 100)

series = pd.Series(arr, name = "Oil")

print(series)

print("When data type of values is float, mean is : ", series.mean())

series = series.astype("int")

print("When data type of values is int, mean is : ", series.mean())











