import pandas as pd
import numpy as np

# Sample data: Daily temperature readings from various cities
data = [
    "Delhi 35", "Mumbai 30", "Chennai 33", "Delhi 36", "Mumbai 29",
    "Chennai 34", "Delhi 38", "Mumbai 28", "Chennai 32", "Delhi 34",
    "Mumbai 31", "Chennai 35", "Delhi 37", "Mumbai 27", "Chennai 31"
]

temperature_series = pd.Series(data, name="City_Temperature")