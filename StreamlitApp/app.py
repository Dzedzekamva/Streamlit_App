import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Loading cleaned dataset
file_path = '/StreamlitApp/cleaned_data.csv'
df = pd.read_csv(file_path)

# Title of the Streamlit app
st.title('Data Insights Dashboard')

# Displaying basic information about the dataset
st.write("### Dataset Overview")
st.write(df.head())  # Display the first 5 rows

# Displaying summary statistics
st.write("### Dataset Summary")
st.write(df.describe())  # Display summary statistics

# Distribution of Maths scores
st.write("### Distribution of Maths Scores")
fig, ax = plt.subplots()
sns.histplot(df['Maths'], kde=True, ax=ax, color='blue')
st.pyplot(fig)

# Scatter plot of Maths vs Reading
st.write("### Interactive Scatter Plot of Maths vs Reading")
fig = px.scatter(df, x='Maths', y='Reading', color='Gender_x', title="Maths vs Reading")
st.plotly_chart(fig)

# Slider to filter data based on Maths scores
st.write("### Filter Data by Maths Scores")
min_math = df['Maths'].min()
max_math = df['Maths'].max()
filtered_data = df[df['Maths'] >= st.slider('Select minimum Maths score', min_math, max_math, min_math)]
st.write(filtered_data)

# Dropdown to filter data by Social Media type
st.write("### Filter Data by Social Media")
social_media_choices = df['Social Media'].unique()
social_media_filter = st.selectbox('Select Social Media Type', social_media_choices)
filtered_social_media_data = df[df['Social Media'] == social_media_filter]
st.write(filtered_social_media_data)

# Displaying AI-Generated Insights (Replace with actual insights from your analysis)
st.write("### AI-Generated Insights")
st.write("The model predicts that the most significant factor affecting student performance is the amount of sleep.")
