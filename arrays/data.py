import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_excel('10.xlsx', header=1)
# data.to_csv('10.csv', sep='\t', index=None)

new_data = pd.read_csv('10.csv', sep='\t', header=None)
xs = new_data.iloc[0, :]
ys = new_data.iloc[1, :]
