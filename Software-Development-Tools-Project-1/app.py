import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the dataset into a Pandas DataFrame
df = pd.read_csv('vehicles_us_cleaned.csv')

# Title of the app centered
st.title('Vehicle Data Dashboard')

st.write("Welcome to the Vehicle Data Dashboard! This app helps analyze and visualize vehicle data.")

# Display dataset preview
st.write("Dataset preview:")
st.write(df.head())

# dataset columns
st.write("Dataset columns:")
st.write(df.columns)

# basic statistics
st.write("Basic statistics:")
st.write(df.describe())


st.header("Visualizations")

# histogram- types of vehicles by manufacturer
st.subheader('Types of Vehicles by Manufacturer')
fig = px.histogram(df, x= 'manufacturer', color= 'type')

st.plotly_chart(fig)



#histogram for the 'price' column
fig = px.histogram(df, x='price', title='Distribution of Vehicle Prices')


#   checkbox
show_histogram = st.checkbox('Show Histogram')
if show_histogram:
    st.plotly_chart(fig)


#histogram for vehicle prices colored by condition
fig_condition = px.histogram(
    df,
    x='price',
    color='condition',
    title='Distribution of Vehicle Prices by Condition',
    labels={'price': 'Price (USD)', 'condition': 'Condition'},
    nbins=30,
    template='plotly_dark'
)
fig_condition.update_layout(
    bargap=0.2,
    xaxis_title='Price (USD)',
    yaxis_title='Number of Vehicles',
)

#------
show_histogram = st.checkbox('Show Histogram by Condition', key='show_histogram_1')
if show_histogram:
    st.plotly_chart(fig_condition)

fig_price = px.histogram(
    df,
    x='price',
    title='Distribution of Vehicle Prices',
    labels={'price': 'Price (USD)'},
    nbins=30
)

show_another_histogram = st.checkbox('Show Histogram of Prices', key='show_histogram_2')
if show_another_histogram:
    st.plotly_chart(fig_price)


#-------------

# scatterplot for Price vs. Odometer
# Check if the required columns exist and drop rows with missing data
required_columns = ['odometer', 'price', 'type']
df = df.dropna(subset=required_columns)

# make sure numeric columns are properly converted
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['odometer', 'price'])  # Drop any rows where conversion failed

# Price vs. Odometer
fig = px.scatter(
    df,
    x='odometer',
    y='price',
    color='type',
    title='Price vs. Odometer by Vehicle Type',
    labels={
        'odometer': 'Odometer Reading (miles)',
        'price': 'Price (USD)',
        'type': 'Vehicle Type'
    },
    hover_data=['manufacturer', 'model_name', 'condition'],  # Additional hover info
    template='plotly_dark'
)
fig.update_layout(
    xaxis_title='Odometer Reading (miles)',
    yaxis_title='Price (USD)',
)

# Checkbox
show_scatterplot = st.checkbox('Show Scatterplot')
if show_scatterplot:
    st.plotly_chart(fig)




#run this code in the terminal to see the output of the code above
    #   streamlit run app.py