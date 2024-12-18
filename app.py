import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset into a Pandas DataFrame
df = pd.read_csv('vehicles_us.csv')

st.header("Vehicle Data Dashboard")

st.write("Welcome to the Vehicle Data Dashboard! This app helps analyze and visualize vehicle data effectively.")


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


#run this code in the terminal to see the output of the code above
    #   streamlit run app.py