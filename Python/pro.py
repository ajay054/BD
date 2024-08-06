# # Skip initial metadata rows and read the actual data
# interest_rates_df_cleaned = pd.read_excel(C:\Users\ajayk\Documents\Project BD\Official_Interest_Rates_Cleaned.csv, sheet_name='6. Official Interest Rates', skiprows=5)

# # Display the first few rows of the cleaned dataframe
# interest_rates_df_cleaned.head()
import pandas as pd

# Corrected file path for CSV file
file_path = r'C:\Users\ajayk\Documents\Project BD\Official_Interest_Rates_Cleaned.csv'

# Skip initial metadata rows and read the actual data
interest_rates_df_cleaned = pd.read_csv(file_path, skiprows=5)

# Display the first few rows of the cleaned dataframe
print(interest_rates_df_cleaned.head())

