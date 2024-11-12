import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

df


# Filter the DataFrame to include only rows where the 'state' column is 'Pahang'
df_NS= df[df['state'] == 'Negeri Sembilan']

df_NS

# prompt: i want mount data from google drive

from google.colab import drive
drive.mount('/content/drive')

import os
import pandas as pd

# Path to the folder
folder_path = '/content/drive/MyDrive/AssignmentDataScience'

# List all files in the folder
files = os.listdir(folder_path)

# Load all CSV files into a list of DataFrames
data = [pd.read_csv(os.path.join(folder_path, file)) for file in files if file.endswith('.csv')]

# Example: Display the first DataFrame
data[0].head()


import pandas as pd

# Assuming 'df_NS' contains Negeri Sembilan data and 'data' is a list of pricecatcher DataFrames
# Create an empty list to store the filtered data
filtered_data = []

# Iterate through the DataFrames from the pricecatcher CSV files
for df_pricecatcher in data:
    # Merge the pricecatcher data with the Negeri Sembilan premise codes
    merged_df = pd.merge(df_pricecatcher, df_NS, on='premise_code', how='inner')
    # Append the filtered data to the list
    filtered_data.append(merged_df)

# Example: Concatenate all the filtered DataFrames into one
if filtered_data:
    final_df = pd.concat(filtered_data)
    # Display the filtered DataFrame as a table
    from IPython.display import display
    display(final_df)
else:
    print("No matching premise codes found in the pricecatcher CSV files.")
# prompt: i want to filter only item code 2

# Assuming 'final_df' contains the merged DataFrame from the previous code
# Filter the DataFrame based on 'item_code'
df_item_code_2 = final_df[final_df['item_code'] == 2]

# Display the filtered DataFrame
display(df_item_code_2)

# Define the file path in your Google Drive
file_path = '/content/drive/My Drive/filtered_item_code_2.csv'  # Change the path as needed

# Save the filtered DataFrame as a CSV file to Google Drive
df_item_code_2.to_csv(file_path, index=False)

print(f"File saved successfully to {file_path}")
