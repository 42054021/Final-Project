import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('Students Performance in Exams')
df = pd.read_csv('exams.csv')

par_filter = st.sidebar.multiselect(
     'Parental level of education:',
     df.parental_level_of_education.unique(),  
     df.parental_level_of_education.unique())  

lunch_filter = st.sidebar.multiselect(
     'The lunch Situation:',
     df.lunch.unique(),  
     df.lunch.unique())  


form = st.sidebar.form("Gender_form")
gender_filter = form.text_input('Gender(enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

form = st.sidebar.form("pre_form")
pre_filter = form.text_input('Preparation conditions(completed or none)', 'ALL')
form.form_submit_button("Apply")

df = df[df.parental_level_of_education.isin(par_filter)]

df = df[df.lunch.isin(lunch_filter)]

if gender_filter!='ALL':
    df = df[df.gender == gender_filter]

if pre_filter!='ALL':
    df = df[df.test_preparation_course == pre_filter]

st.subheader('Exams Details:')
st.write(df[['gender', 'parental_level_of_education', 'lunch','test_preparation_course','math_score','reading_score','writing_score']])

st.subheader('Histogram of the math score')
fig, ax = plt.subplots(figsize=(10, 5))
df['math_score'].plot.hist(bins=10,color='blue')
st.pyplot(fig)

st.subheader('math score By Parental level of education')
fig, ax = plt.subplots(figsize=(10, 5))
mean = df.groupby('parental_level_of_education')['math_score'].mean()
mean.plot.bar(ax=ax,color='yellow')
st.pyplot(fig)

st.subheader('The correlation between reading scores and writing scores')
fig, ax = plt.subplots(figsize=(10, 5))
df.plot.scatter(x='reading_score', y='writing_score',ax=ax,color='green')
st.pyplot(fig)


