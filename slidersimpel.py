import streamlit as st
import matplotlib.pyplot as plt

import numpy as np

# # data to be plotted
a = st.slider('Silakan pilih diameter dalam', 0, 1.0, 0.2,0.05)
b = st.slider('Silakan pilih diameter luar', 0, 1.0, 0.2,0.05)
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

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)*a+b
sd = statistics.stdev(x_axis)*a+b

fig2 = plt.figure()
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.plot(x_axis, norm.pdf(x_axis, mean2, sd2))
plt.plot(x_axis, norm.pdf(x_axis, mean3, sd3))
plt.show()
st.pyplot(fig2)

