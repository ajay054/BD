import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Hide the root Tkinter window
Tk().withdraw()

# Open a file dialog to select the CSV file
csv_input_path = askopenfilename(filetypes=[("CSV files", "*.csv")])

if csv_input_path:
    # Open a file dialog to select the output CSV file location
    csv_output_path = asksaveasfilename(defaultextension=".csv",
                                        filetypes=[("CSV files", "*.csv")],
                                        initialfile="Cleaned_Interest_Rates.csv")
    
    if csv_output_path:
        try:
            # Read the CSV file, skipping initial metadata rows
            interest_rates_df_cleaned = pd.read_csv(csv_input_path, skiprows=5)
            
            # Save the DataFrame to a new CSV file
            interest_rates_df_cleaned.to_csv(csv_output_path, index=False)
            
            print(f'DataFrame successfully saved to {csv_output_path}')
        except FileNotFoundError:
            print(f'File not found: {csv_input_path}')
        except Exception as e:
            print(f'An error occurred: {e}')
    else:
        print('No output file selected.')
else:
    print('No input file selected.')
