import streamlit as st
import time

st.title('Tieu de cua website')
st.write('Xin chao')
name = st.text_input('Type your name')
# a = st.button("Show the name",1)
if st.button("Show the name", ''):
  st.balloons()

my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.01)
  my_bar.progress(percent_complete + 1)
