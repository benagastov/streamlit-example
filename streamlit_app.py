import streamlit as st

# Use widgets' returned values in variables:
for i in range(int(st.number_input('Num:'))):
 foo()
if st.sidebar.selectbox('I:',['f']) == 'f':
  b()
my_slider_val = st.slider('Quinn Mallory', 1, 88)
st.write(slider_val)
