import streamlit as st
import pandas as pd

st.title('A simple app')

myslider = st.slider('Celsius')
st.write(myslider, 'in Farentheit is', myslider * 9/5 + 32)

myslider2 = st.slider('Inch')
st.write(myslider2, 'in cm is', myslider2 * 2.54)

myslider3 = st.slider('Feet')
st.write(myslider3, 'in cm is', myslider3 * 30.48)

data = pd.read_csv('students.csv')

df = pd.DataFrame(data)

st.subheader('Automate with streamlit')
st.write('''Student Score
Enjoy it!
''')

df = df.melt(id_vars=['Module'], var_name='student', value_name='Score')
df['Score'] = df['Score'].fillna(0)
df['Module'] = df['Module'].astype(str)
df['student'] = df['student'].astype(str)

Group_choice = st.selectbox("Student_ID:", df.student)
st.write(df)


