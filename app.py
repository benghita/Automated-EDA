import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#from data_processor import preprocess_data

def main():
    st.title("Automated EDA Tool")
    
    # Upload a CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
        # Preprocess the data
        preprocessed_data = preprocess_data(data)
        
        st.subheader("Preprocessed Data")
        st.write(preprocessed_data)
        
        # Data Visualization
        st.subheader("Data Visualization")
        column_names = preprocessed_data.columns
        
        selected_column = st.selectbox("Select a column", column_names)
        
        if selected_column:
            st.write(f"Visualization for {selected_column}")
            
            if preprocessed_data[selected_column].dtype == "float64" or preprocessed_data[selected_column].dtype == "int64":
                st.write("Histogram:")
                plt.figure(figsize=(8, 6))
                sns.histplot(preprocessed_data[selected_column], bins=20, kde=True)
                st.pyplot()
                
                st.write("Box Plot:")
                plt.figure(figsize=(8, 6))
                sns.boxplot(x=preprocessed_data[selected_column])
                st.pyplot()
                
            elif preprocessed_data[selected_column].dtype == "object":
                st.write("Count Plot:")
                plt.figure(figsize=(8, 6))
                sns.countplot(x=preprocessed_data[selected_column])
                st.pyplot()
                
            # Add more visualizations for other data types
    
if __name__ == "__main__":
    main()
