import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

df
st.write(df)

# Filter the DataFrame to include only rows where the 'state' column is 'Pahang'
df_NS= df[df['state'] == 'Negeri Sembilan']

df_NS
st.write(df_NS)

import streamlit as st
import pandas as pd
import zipfile
import io
import os

# Allow the user to upload a zip file containing multiple CSV files
uploaded_zip = st.file_uploader("Upload a ZIP file containing multiple CSV files", type="zip")

if uploaded_zip is not None:
    # Create a folder to extract the files
    with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
        # Extract all files into memory, you can also extract into disk if needed
        zip_ref.extractall("temp_folder")

    # List all CSV files from the extracted folder
    csv_files = [f for f in os.listdir("temp_folder") if f.endswith('.csv')]

    # Load all CSV files into a list of DataFrames
    data = [pd.read_csv(os.path.join("temp_folder", file)) for file in csv_files]

    # Display the first DataFrame as an example
    if data:
        st.write(f"Loaded {len(data)} CSV files.")
        st.write("First CSV file contents:")
        st.dataframe(data[0])

        # Filter the DataFrame to include only rows where the 'state' column is 'Negeri Sembilan'
        df_NS = data[0][data[0]['state'] == 'Negeri Sembilan']
        st.write("Filtered Data for 'Negeri Sembilan':")
        st.dataframe(df_NS)

        # Merge the pricecatcher data with the Negeri Sembilan premise codes
        filtered_data = []
        for df_pricecatcher in data:
            # Merge with Negeri Sembilan data based on 'premise_code'
            merged_df = pd.merge(df_pricecatcher, df_NS, on='premise_code', how='inner')
            filtered_data.append(merged_df)

        # Concatenate all the filtered DataFrames into one
        if filtered_data:
            final_df = pd.concat(filtered_data)
            st.write("Filtered and Merged DataFrame:")
            st.dataframe(final_df)

            # Filter for 'item_code' 2
            df_item_code_2 = final_df[final_df['item_code'] == 2]
            st.write("Filtered Data for 'item_code' 2:")
            st.dataframe(df_item_code_2)

            # Provide an option to download the filtered DataFrame as a CSV
            if not df_item_code_2.empty:
                csv = df_item_code_2.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Filtered CSV",
                    data=csv,
                    file_name='filtered_item_code_2.csv',
                    mime='text/csv',
                )
        else:
            st.write("No matching premise codes found in the pricecatcher CSV files.")
    else:
        st.write("No CSV files were found in the uploaded ZIP.")
else:
    st.write("Please upload a ZIP file containing CSV files.")

