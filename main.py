import streamlit as st
import pandas as pd

myslider = st.slider('Celsius')
st.write(myslider, 'in Farentheit is', myslider * 9/5 + 32)

myslider2 = st.slider('Inch')
st.write(myslider2, 'in cm is', myslider2 * 2.54)

myslider3 = st.slider('Feet')
st.write(myslider3, 'in cm is', myslider2 * 30.48)


data = {
  'Series_1':[1,3,4,5,7],
  'Series_2':[10,30,40,100,250]
}

df = pd.DataFrame(data)

st.title('A simple app')
st.subheader('Automate with streamlit')
st.write('''first app.
Enjoy it!
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)


