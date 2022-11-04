
#importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin
from math import pi
from scipy.fft import rfft, rfftfreq, ifft
 
N=600000 #sampling rate
# Parametera of the FM wave
vc=4
fc=10000
vm=10
fm=1000
kf=500
df=kf*vm
mf= df/fm

# Generating the FM wave
t= np.linspace(0,1,N)
FM= vc*cos(2*pi*fc*t + mf*cos(2*pi*fm*t))

# Generating the frequency spectrum of the FM wave
freq_spectrum= rfft(FM)
freq= rfftfreq(N,1/N)

# Calculating the bandwidth of the FM wave
bw=0
for f in range(fc,int(freq.size)):

  if np.abs((freq_spectrum[f])/N) > 0.1:
    bw=f
BW= ((bw-fc)*2)

# Ploting the FM wave
plt.subplot(2,1,1)
plt.plot(t,FM)
plt.title("FM wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.xlim(0, 0.009)
plt.text(0, 5, "modulation index = " + str(mf) + '\n' + 'Bandwidth = ' + str(BW), fontsize=14)
# Ploting the FM wave spectrun
plt.subplot(2,1,2)
plt.plot(freq,np.abs(freq_spectrum)/N)
plt.title("FM wave spectrum")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.xlim(0, 20000)

plt.subplots_adjust(hspace=0.5)
plt.rc('font', size=12)
fig = plt.gcf()
fig.set_size_inches(16, 9)
plt.show()