# in python 
# input
# df has name , place ,countrycode
# dict has key
#  as countrycode and value as countryname.

# output 
# dataframe must have 4 columns name , place ,countrycode, countryname


# import pandas as pd

# # Sample DataFrame
# data = {
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'place': ['New York', 'Los Angeles', 'Chicago'],
#     'countrycode': ['US', 'US', 'US']
# }
# df = pd.DataFrame(data)

# # Sample dictionary
# country_dict = {
#     'US': 'United States',
#     'CA': 'Canada',
#     'MX': 'Mexico'
# }

# # Map the dictionary to the DataFrame
# df['countryname'] = df['countrycode'].map(country_dict)

# # Display the resulting DataFrame
# print(df)
import pandas as pd

# Sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'], 'place': ['New York', 'Los Angeles', 'Chicago'], 'countrycode': ['US', 'US', 'US']}
df = pd.DataFrame(data)

# Sample dictionary
country_dict = {'US': 'United States', 'CA': 'Canada', 'MX': 'Mexico'}

# Add countryname column
df['countryname'] = df['countrycode'].map(country_dict)

print(df)
