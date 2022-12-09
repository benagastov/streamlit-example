import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

import streamlit as st

st.write(f'''
    <a target="_self" href="https://benagastov.github.io/mpic.github.io/Page-12.html">
        <button>
            Next
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["📈 Grafik Awal", "🗃 Grafik Kustom"])
with tab1:
  st.subheader("Grafik Sensitivitas Massa yang Dipengaruhi Diameter Elektroda, Massa Gas dan Frekuensi")
  col1, col2 = st.columns([7, 1.5])
  
  with col2:
    image = Image.open('Mamako_hugging2.png')
    st.image(image, caption='Google Ads')
    image2 = Image.open('Konosuba_Darkness.jpg')
    st.image(image2)
  with col1:
    # Plot between -10 and 10 with .001 steps.
    x_axis = np.arange(-8, 8, 0.01)

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
    plt.ylabel('Mass Sensitivity (Hz/Kg)')
    plt.xlabel('Diameter Elektroda (mm)')
    st.pyplot(fig)
    st.write("Grafik Meniru Hasil Jurnal dengan densitas massa = 1 µg/mm2")
    
    image3 = Image.open('Plot Sesungguhnya.JPG')
    st.image(image3, caption='Plot yang dikutip dari Jurnal Analysis of the Radial Dependence of Mass Sensitivity for Modified-Electrode Quartz Crystal Resonators')


with tab2:
  #create your figure and get the figure object returned
  st.subheader("Grafik Sensitivitas Massa dengan Diameter Variabel")
  # t1 = np.arange(0.0, rentangmax, 0.1)
  # plt.plot(np.cos(t1*np.pi), color='tab:orange', linestyle='--', marker='.') 
  # # data to be plotted
  dm1 = st.slider('Silakan pilih diameter dalam cincin 1', 0.0, 1.0, 0.2,0.05)
  dm2 = st.slider('Silakan pilih diameter luar cincin 1', 0.0, 1.0, 0.2,0.05)
  dm3 = st.slider('Silakan pilih diameter dalam cincin 2', 0.0, 1.0, 0.5,0.05)
  dm4 = st.slider('Silakan pilih diameter luar cincin 2', 0.0, 1.0, 0.5,0.05)
  st.write("diameter dalam cincin 1 sebesar ", dm1, 'nm')
  st.write("dan diameter luar cincin 1 sebesar ", dm2, 'nm')
  st.write("diameter dalam cincin 2 sebesar ", dm3, 'nm')
  st.write("dan diameter luar cincin 2 sebesar ", dm4, 'nm')


  # Calculating mean and standard deviation
  mean4 = statistics.mean(x_axis)*dm1+dm2
  sd4 = statistics.stdev(x_axis)*dm1+dm2
  mean5 = statistics.mean(x_axis)*dm3+dm4
  sd5 = statistics.stdev(x_axis)*dm3+dm4

  fig2 = plt.figure()
  plt.plot(x_axis, norm.pdf(x_axis, mean4, sd4))
  plt.plot(x_axis, norm.pdf(x_axis, mean5, sd5))
  plt.ylabel('Mass Sensitivity (Hz/Kg)')
  plt.xlabel('Diameter Elektroda (mm)')
  plt.show()
  st.pyplot(fig2)

