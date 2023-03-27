import pandas as pd

#1. Input
raw_data = pd.read_csv("menu.csv")


#2. Process
numberofitems = len(raw_data)
sorted_menu = raw_data.sort_values("Menu",ascending = True)

#3. Output
print(f'#1 -> Count: {numberofitems}')
print(f'#2 {sorted_menu}')