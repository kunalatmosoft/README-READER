import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(
    page_title="Streamlit Analytics Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Description
st.title("Streamlit Analytics Platform")
st.markdown("""
This is an interactive analytical platform using built-in datasets from the **Seaborn** library.
Explore datasets, visualize trends, and gain insights in one place!
""")

# Sidebar: Dataset selection
datasets = {
    "Iris": sns.load_dataset("iris"),
    "Titanic": sns.load_dataset("titanic"),
    "Tips": sns.load_dataset("tips"),
    "Penguins": sns.load_dataset("penguins"),
}

selected_dataset_name = st.sidebar.selectbox("Select a Dataset", list(datasets.keys()))
data = datasets[selected_dataset_name]

# Display dataset details
st.subheader(f"Dataset: {selected_dataset_name}")
st.write("### Data Preview", data.head())
st.write("### Summary Statistics", data.describe(include='all'))

# Sidebar: Visualization Options
st.sidebar.markdown("### Visualization Settings")
plot_type = st.sidebar.selectbox(
    "Select Plot Type",
    ["Scatter Plot", "Histogram", "Box Plot", "Bar Plot"]
)

x_axis = st.sidebar.selectbox("X-Axis", options=data.columns)
y_axis = st.sidebar.selectbox("Y-Axis", options=data.columns)
hue = st.sidebar.selectbox("Hue (Optional)", options=[None] + list(data.columns))

# Visualization
st.subheader("Visualization")
fig, ax = plt.subplots(figsize=(10, 6))

if plot_type == "Scatter Plot":
    sns.scatterplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)
elif plot_type == "Histogram":
    sns.histplot(data=data, x=x_axis, hue=hue, kde=True, ax=ax)
elif plot_type == "Box Plot":
    sns.boxplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)
elif plot_type == "Bar Plot":
    sns.barplot(data=data, x=x_axis, y=y_axis, hue=hue, ax=ax)

st.pyplot(fig)

# Advanced Analysis: Correlation Heatmap
if st.checkbox("Show Correlation Heatmap"):
    st.subheader("Correlation Heatmap")
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Footer
st.markdown("""
---
Built with [Streamlit](https://streamlit.io/) and [Seaborn](https://seaborn.pydata.org/).
""")
