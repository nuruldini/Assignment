import streamlit as st
import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

# Delete the first column
df = df.drop(df.columns[0], axis=1)

# Display the DataFrame without the first column using Streamlit
st.write(df)

# Filter the DataFrame to include only rows where the 'state' column is 'Negeri Sembilan'
df_NS = df[df['state'] == 'Negeri Sembilan']

# Display the filtered DataFrame
st.write(df_NS)
