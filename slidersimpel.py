import streamlit as st
import matplotlib.pyplot as plt

import numpy as np

# data to be plotted
rentangmax = st.slider('Berapa rentang max yang kamu inginkan?', 0, 130, 25)
st.write("rentang max nya sebesar ", rentangmax, 'satuan')

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-20, 20, 0.01)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)*0.4
sd = statistics.stdev(x_axis)*0.4
mean2 = statistics.mean(x_axis)*0.8
sd2 = statistics.stdev(x_axis)*0.8
mean3 = statistics.mean(x_axis)*0.25
sd3 = statistics.stdev(x_axis)*0.25

fig = plt.figure()
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.plot(x_axis, norm.pdf(x_axis, mean2, sd2))
plt.plot(x_axis, norm.pdf(x_axis, mean3, sd3))
plt.show()


#create your figure and get the figure object returned

# t1 = np.arange(0.0, rentangmax, 0.1)
# plt.plot(np.cos(t1*np.pi), color='tab:orange', linestyle='--', marker='.') 

st.pyplot(fig)

