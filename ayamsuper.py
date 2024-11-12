import streamlit as st
import pandas as pd

# Allow users to upload CSV files through Streamlit
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display the DataFrame
    st.write("Data from uploaded CSV:")
    st.dataframe(df)
    
    # Filter the DataFrame to include only rows where the 'state' column is 'Negeri Sembilan'
    df_NS = df[df['state'] == 'Negeri Sembilan']
    st.write("Filtered Data for 'Negeri Sembilan':")
    st.dataframe(df_NS)
    
    # Filter for 'item_code' 2
    df_item_code_2 = df_NS[df_NS['item_code'] == 2]
    st.write("Filtered Data for 'item_code' 2:")
    st.dataframe(df_item_code_2)
    
    # Save the filtered data as CSV
    if not df_item_code_2.empty:
        st.write("Download the filtered data:")
        csv = df_item_code_2.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='filtered_item_code_2.csv',
            mime='text/csv',
        )
else:
    st.write("Please upload a CSV file.")
