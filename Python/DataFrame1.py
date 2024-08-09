# python

# df with 3 cols sourcecode,intermeidatecode,targetcode.
# ABC12,SCR,ABC12_2005f
# DFG,ab,345-dfg

# I want output dataframe as
# sourcecode,intermeidatecode,targetcode, modifiedcode
# ABC12,SCR,ABC12_2005f,SCR_2005f
# DFG,ab,345-dfg,ab-345



import pandas as pd

# Sample DataFrame
data = {
    'sourcecode': ['ABC12', 'DFG'],
    'intermeidatecode': ['SCR', 'ab'],
    'targetcode': ['ABC12_2005f', '345-dfg']
}
df = pd.DataFrame(data)

# Function to create modifiedcode
def create_modified_code(row):
    if row['intermeidatecode'] in row['targetcode']:
        # Replace sourcecode with intermeidatecode in targetcode
        return row['targetcode'].replace(row['sourcecode'], row['intermeidatecode'])
    else:
        # Concatenate intermeidatecode with the first two characters of targetcode
        return row['intermeidatecode'] + '-' + row['targetcode'][:2]

# Apply the function to each row
df['modifiedcode'] = df.apply(create_modified_code, axis=1)

print(df)
