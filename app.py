import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Exploratory Data Analysis and Visualization App")

# Upload CSV File
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read and display the data
    df = pd.read_csv(uploaded_file)
    st.write("## Dataset Preview")
    st.dataframe(df)

    # Missing Values Analysis
    st.write("## Missing Values Analysis")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])

    # Data Cleaning (Example: Drop or Fill Missing Values)
    st.write("## Data Cleaning Options")
    clean_option = st.selectbox("Choose a method to handle missing values:", ["Drop Rows", "Fill with Mean"])
    
    if clean_option == "Drop Rows":
        df = df.dropna()
    elif clean_option == "Fill with Mean":
        df = df.fillna(df.mean())

    st.write("Data after cleaning:")
    st.dataframe(df)

    # EDA - Display Summary Statistics
    st.write("## Exploratory Data Analysis (EDA)")
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.write("### Data Visualization")
    visualization = st.selectbox("Choose a visualization:", ["Histogram", "Correlation Heatmap"])
    
    if visualization == "Histogram":
        column = st.selectbox("Select Column for Histogram:", df.columns)
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column].dropna(), kde=True)
        st.pyplot(plt)

    elif visualization == "Correlation Heatmap":
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)
