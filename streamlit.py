import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# App Title
st.title("Best Streamlit App in One Page")

# Display a description
st.markdown("""
This is a demo of a **Streamlit app** that showcases multiple features:
- Displaying a dataset.
- Interactive plots.
- Simple machine learning.
- A text input form.
""")

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Show dataset
st.header("Iris Dataset")
st.write(df.head())

# Display a summary of the dataset
st.subheader("Dataset Summary")
st.write(df.describe())

# Interactive feature: Select a feature for a plot
st.sidebar.header("Choose a feature to plot")
feature = st.sidebar.selectbox("Select a feature", df.columns[:-1])  # Exclude 'species'

# Plotting
st.subheader(f"Distribution of {feature}")
sns.histplot(df[feature], kde=True)
st.pyplot()

# Add interactive text input to take user input
st.subheader("User Input Form")
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

# Add a simple ML model: Iris Species Prediction
st.subheader("Iris Species Prediction")
sepal_length = st.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Simple ML model (using a dummy model here for simplicity)
dummy_model = lambda x: iris.target_names[np.random.choice([0, 1, 2])]  # Random prediction

# Make prediction
if st.button("Predict Species"):
    prediction = dummy_model([sepal_length, sepal_width, petal_length, petal_width])
    st.write(f"Predicted Species: {prediction}")

# Footer information
st.markdown("---")
st.markdown("This is a basic example of a Streamlit app.")
st.markdown("You can extend this with more complex features, customizations, and data.")
