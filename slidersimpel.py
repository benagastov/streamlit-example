import streamlit as st
import matplotlib.pyplot as plt

import numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")


# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-8, 8, 0.01)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)*0.4
sd = statistics.stdev(x_axis)*0.4
mean2 = statistics.mean(x_axis)*0.8
sd2 = statistics.stdev(x_axis)*0.8
mean3 = statistics.mean(x_axis)*0.25
sd3 = statistics.stdev(x_axis)*0.25

tab1.fig = plt.figure()
tab1.plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
tab1.plt.plot(x_axis, norm.pdf(x_axis, mean2, sd2))
tab1.plt.plot(x_axis, norm.pdf(x_axis, mean3, sd3))
tab1.plt.show()
tab1.st.pyplot(fig)

#create your figure and get the figure object returned
tab2.subheader("A tab with the data")
# t1 = np.arange(0.0, rentangmax, 0.1)
# plt.plot(np.cos(t1*np.pi), color='tab:orange', linestyle='--', marker='.') 
# # data to be plotted
tab2.dm1 = st.slider('Silakan pilih diameter dalam', 0.0, 1.0, 0.2,0.05)
tab2.dm2 = st.slider('Silakan pilih diameter luar', 0.0, 1.0, 0.2,0.05)
tab2.st.write("diameter dalam nya sebesar ", dm1, 'nm')
tab2.st.write("dan diameter luar nya sebesar ", dm2, 'nm')


# Calculating mean and standard deviation
mean4 = statistics.mean(x_axis)*dm1+dm2
sd4 = statistics.stdev(x_axis)*dm1+dm2

tab2.fig2 = plt.figure()
tab2.plt.plot(x_axis, norm.pdf(x_axis, mean4, sd4))
tab2.plt.show()
tab2.st.pyplot(fig2)

