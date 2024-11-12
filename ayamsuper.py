import pandas as pd

# Load the dataset from the CSV file
file_path = 'https://raw.githubusercontent.com/nuruldini/Assignment/refs/heads/main/lookup_premise.csv'
df = pd.read_csv(file_path)

df


# Filter the DataFrame to include only rows where the 'state' column is 'Pahang'
df_NS= df[df['state'] == 'Negeri Sembilan']

df_NS

import streamlit as st
import pandas as pd
import io

# Allow the user to upload multiple CSV files
uploaded_files = st.file_uploader("Upload up to 15 CSV files", type="csv", accept_multiple_files=True)

if uploaded_files is not None and len(uploaded_files) > 0:
    if len(uploaded_files) > 15:
        st.error("You can upload a maximum of 15 CSV files at once.")
    else:
        # Load all uploaded CSV files into a list of DataFrames
        data = [pd.read_csv(file) for file in uploaded_files]

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
            st.write("No CSV files were found in the uploaded files.")
else:
    st.write("Please upload up to 15 CSV files.")
