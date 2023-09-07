import pandas as pd

pd.set_option('display.max_rows',10)

import numpy as np

reviews =pd.read_csv('data\winemag-data-130k-v2.csv.zip', index_col = 0)

country_counts = reviews.country.value_counts()


print(country_counts)








