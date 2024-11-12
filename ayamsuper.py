import streamlit as st
import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

# Display the DataFrame
st.write(df)

# Filter the DataFrame to include only rows where the 'state' column is 'Negeri Sembilan'
df_NS = df[df['state'] == 'Negeri Sembilan']

# Reset the index and create a new column with sequential numbers for 'bill number'
df_NS['bill number'] = range(1, len(df_NS) + 1)

# Display the updated filtered DataFrame
st.write(df_NS)
