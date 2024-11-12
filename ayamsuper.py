import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

df


# Filter the DataFrame to include only rows where the 'state' column is 'Pahang'
df_NS= df[df['state'] == 'Negeri Sembilan']

df_NS


