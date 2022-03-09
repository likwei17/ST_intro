import streamlit as st
import pandas as pd

st.title('A simple dimple App')

myslider = st.slider('Celsius')
st.write(myslider, 'in Farentheit is', myslider * 9/5 + 32)

myslider2 = st.slider('Inch')
st.write(myslider2, 'in cm is', myslider2 * 2.54)

myslider3 = st.slider('Feet')
st.write(myslider3, 'in cm is', myslider3 * 30.48)

st.set_page_config(layout = "wide")
st.subheader('Score Metrics')
st.write('''Scorecard for students''')

data = pd.read_csv('students.csv')

df = pd.DataFrame(data)
#df = df.melt(id_vars=['Module'], var_name='student', value_name='Score')
#print (df)
dff = df[(df['Student'].astype(str).str[:4] == 'MA21')]
dff.set_index('Student', inplace = True)
#print(dff)

#print(dff.dtypes)
# slist = dff['student'].unique()
# print(slist)
# student = st.sidebar.selectbox("Select a student:",slist)

# fig = px.line(df[df['student'] == student], 
#     x = "Module", y = "Score", title = student)
st.bar_chart(dff)


