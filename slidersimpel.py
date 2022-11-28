import streamlit as st
import matplotlib.pyplot as plt

import numpy as np

# data to be plotted
rentangmax = st.slider('Berapa rentang max yang kamu inginkan?', 0, 130, 25)
st.write("rentang max nya sebesar ", rentangmax, 'satuan')

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot(np.arange(0.0, rentangmax, 0.1), np.cos(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.') 

st.pyplot(fig)

