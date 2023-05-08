import pandas as pd
import os

BASE_PATH = 'bbc'
CATS = ['business', 'entertainment', 'politics', 'sport', 'tech']

data = []
for cat in CATS:
    print(f'Processing {cat} data...')
    path = os.path.join(BASE_PATH, cat)
    files = os.listdir(path)
    for file in files:            # iterate through file
        with open(os.path.join(path, file), 'r') as f:
            text = f.read()           # read text
            text = text.replace('\n', ' ')  # remove new line
        data.append({'text': text, 
                     'category': cat})  # append to list
    

print('Saving data ...')
# convert dictionary to dataframe
df = pd.DataFrame(data)
df.to_csv('bbc_data.csv', index=False)