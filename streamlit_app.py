import streamlit as st

# importing the library
import numpy as np
import pandas as pd

# data to be plotted
rentangmax = st.slider('Berapa rentang max yang kamu inginkan?', 0, 130, 25)
st.write("rentang max nya sebesar ", rentangmax, 'satuan')
x = np.arange(1, rentangmax)
y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
 


chart_data = pd.DataFrame(
    np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100]),
    columns=['a'])

st.line_chart(chart_data)

