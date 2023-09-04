#!/usr/bin/env python
# coding: utf-8

# In[576]:


import re

def extract_data(filename):
    with open(filename, 'r') as file:
        content = file.read()
        
        matches = re.findall(r'[a-zA-Z0-9:]{17}|-\d{2}', content)
        
        data_dict = {matches[i]: int(matches[i+1]) for i in range(0, len(matches), 2)}
        
        return data_dict

filename = '/Users/ruocheng.gu/Desktop/data/floor6/loc29/IR-08-03-10-41.txt'
extracted_data = extract_data(filename)


# for mac_address, signal_strength in extracted_data.items():
#     print(mac_address, signal_strength)

import pandas as pd

data_df = pd.DataFrame(list(extracted_data.items()), columns=["BSSID", "Signal Strength"])

# print(data_df)
import pandas as pd

original_csv_file = '/Users/ruocheng.gu/Desktop/IRBSSID/F6/bssid-08-03-10-41.csv'
df_original = pd.read_csv(original_csv_file)

bssid_column = data_df["BSSID"]
signal_strength_column = data_df["Signal Strength"]

new_df = pd.concat([bssid_column, signal_strength_column], axis=1)

new_df.columns = ["BSSID", "Signal Strength"]

result_df = df_original.merge(new_df, on="BSSID", how="left")
result_csv_file = '/Users/ruocheng.gu/Desktop/IRBSSID/F6/bssid-08-03-10-41.csv'
result_df.to_csv(result_csv_file, index=False)


print(1)


# In[ ]:




