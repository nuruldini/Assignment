import streamlit as st
import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

st.write(df)
# Filter the DataFrame to include only rows where the 'state' column is 'Negeri Sembilan'
df_NS = df[df['state'] == 'Negeri Sembilan']

# Reset the index and drop the old index column
df_NS_reset = df_NS.reset_index(drop=True)

# Display the updated DataFrame without the old index
st.write(df_NS_reset)
