import streamlit as st
<<<<<<< HEAD
import pandas as pd
import plotly.express as px

# Read the dataset into a Pandas DataFrame
df = pd.read_csv('vehicles_us.csv')

# Display dataset preview
st.write("Dataset preview:")
st.write(df.head())

# Display dataset columns
st.write("Dataset columns:")
st.write(df.columns)

# Display basic statistics
st.write("Basic statistics:")
st.write(df.describe())

# Create and display a histogram for the 'price' column
fig = px.histogram(df, x='price', title='Distribution of Vehicle Prices')

# Add checkbox to toggle the histogram
show_histogram = st.checkbox('Show Histogram')
if show_histogram:
    st.plotly_chart(fig)

# Create and display a scatter plot for 'mileage' vs 'price'
fig2 = px.scatter(df, x='odometer', y='price', title='Odometer vs Price')
# Add checkbox to toggle the scatter plot
show_scatter = st.checkbox('Show Scatter Plot')
if show_scatter:
    st.plotly_chart(fig2)
=======
>>>>>>> f514f1141260cb95d921172ce5bb0b6bb59eedc1
