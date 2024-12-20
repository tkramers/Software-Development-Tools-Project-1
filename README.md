# Software-Development-Tools-Project
Sprint4

# Vehicle Data Dashboard

## Project Overview
In this project, I focused on core software engineering tasks to enhance my data skills. My work involves creating and managing Python virtual environments, developing a web application, and deploying it to a public cloud service, Render.

## Description
This is a Streamlit-based web application that displays insights from the `vehicles_us.csv` dataset. The app includes interactive visualizations such as histograms and scatter plots, allowing users to explore vehicle pricing and mileage trends.

## Instructions:
**Step 1. Getting started**
- Create an account on github.com.
- Create a new git repository with a README.md file and a .gitignore file (choose a Python template).
- Make a new Python environment. Install the following packages: pandas, streamlit, plotly.express, and altair. Feel free to install more packages if you want to implement additional features in your web app.
- Create an account on render.com and link it to your GitHub account.
- Use git to clone your new project’s git repository to your local machine. From now on, you’ll be working on the project on your local machine, and then committing and pushing the changes back to the GitHub repository.
- Install VS Code and load the project into VS Code (by opening the project directory with VS Code).
- If you have not used VS Code before, check out the extra lessons on Working in VS Code and Source Control in VS Code.
- In VS Code, set the Python interpreter to the one used by the virtual environment. Make sure you have the necessary packages installed.

**Step 2. Download the data file**
- Download the car advertisement dataset (vehicles_us.csv) or find your own dataset in a CSV format.
- Place the dataset in the root directory of the project.

**Step 3. Exploratory Data Analysis**
- Create an EDA.ipynb Jupyter notebook in VS Code.
- Save the notebook in the notebooks directory of your project.
- Perform some basic exploratory analysis of the dataset in the notebook.
- Create a couple of histograms and scatterplots using plotly-express library.

**Step 4. Develop the web application dashboard**
Note that this is not the same development flow that we used in the lesson on rendering.
- Create an app.py file in the root of the project’s directory. The following steps (2-4) will require you to write code into this app.py file.
- In the app.py file, import streamlit, pandas, and plotly.express.
- Read the dataset’s CSV file into a Pandas DataFrame.
- From the Jupyter notebook, create and/or copy:
 - at least one st.header with text
 - at least one Plotly Express histogram using st.write or st.plotly_chart
 - at least one Plotly Express scatter plot using st.write or st.plotly_chart
 - at least one checkbox using st.checkbox that changes the behavior of any of the above components
- Don’t forget to update the README file when you are done. It should contain a basic description of the project, explaining that this is a tool to simulate random events, and the methods and libraries used to implement it. It should also contain instructions on how other people could launch your project on their local machine if they wanted to.
- IMPORTANT: Your project will only build on the online service if all project files are present in your GitHub repository. Therefore, you must commit and push each new file change to your repository as soon as you’ve comp

**Step 5: Deployment to Render**
- Added a streamlit configuration file to the GitHub repository.
- Created a new web service linked to the GitHub repository in Render.
- Configured the Render web service to install necessary packages and run the app.py file.
- Deployed the final version of the application on Render.
- Verify that your application is accessible at the following URL: https://<APP_NAME>.onrender.com/

## Libraries Used
- Streamlit
- Pandas
- Plotly Express

## How to Run Locally
1. Clone the repository:
git clone <repo-url>

2. Navigate to the project directory:
cd <project-folder>

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
streamlit run app.py