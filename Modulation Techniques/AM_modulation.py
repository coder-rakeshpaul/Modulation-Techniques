
#importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos
from math import pi
from scipy.fft import rfft, rfftfreq, irfft

def message_signal():
  N=600000              #number of samples
  t=np.linspace(0,1,N)  #duration
  
  msg1=Am1*cos(2*pi*t*fm1) # message signal 1
  msg2=Am2*cos(2*pi*fm2*t)  # message signal 2
  msg= msg1+msg2             #multiplexed message signal

  #ploting of message signals
# 1st message signal
  plt.subplot(6,2,1)
  plt.plot(t[:2000],msg1[:2000])
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("1st message signal")
# 2nd message signal
  plt.subplot(6,2,2)
  plt.plot(t[:2000],msg2[:2000])
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("2nd message signal")
# multiplexed  message signal
  plt.subplot(6,2,3)
  plt.plot(t[:2000],msg[:2000])
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("multiplexed message signal")
  return msg , t, N

def am_modulation(Ac,Am1,Am2,fc,fm1,fm2):
  msg , t, N= message_signal()  # getting the message signal
  am= cos(2*pi*fc*t)*(Ac+msg)  #amplitude modulated signal

  #ploting the amplitude modulated signal 
  plt.subplot(6,2,4)
  plt.plot(t[:2000],am[:2000])
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("amplitude modulated wave ")

#spectrum of AM signal
  spectrum_AM= (rfft(am)) 
  frequency= rfftfreq(N,1/N)

  #ploting the spectruum of AM signal
  plt.subplot(6,2,5)
  plt.plot(frequency[:40000],(spectrum_AM/N)[:40000])
  plt.title("amplitude modulated wave spectrun")
  plt.xlabel("frequency")
  plt.ylabel("amplitude")

  demodulation(signal=am,t=t,frequency=frequency,N=N)

 #demodulating the AM signal
def demodulation(signal,t,frequency,N):

#demodulated signal
#speparating the lower frequency components from the higher
  demodulated_signal= signal*cos(2*pi*t*fc) 
  transform_demodulated= rfft(demodulated_signal) 

   #low pass filter
  filter = [0]*(frequency.size)
  for f in range(frequency.size):
    if frequency[f] > -(fm2+50) and frequency[f] < (fm2+50):
        filter[f] = 1
   # output spectrum of the multiplexed signal       
  output_msg_spectrum = transform_demodulated * np.array(filter)
  plt.subplot(6,2,6)
  plt.plot(frequency[:5000],(output_msg_spectrum/N)[:5000])
  plt.xlabel("freqency")
  plt.ylabel("amplitude")
  plt.title("spectrum of output wave")

# recovering the multiplexed signal from its output spectrum
  output_msg_wave=irfft(output_msg_spectrum)
  plt.subplot(6,2,7)
  plt.plot(t[:2000],output_msg_wave[:2000])
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("output multiplexed message wave ")

  #filter to separate the 2nd message signals 
  filter = [0]*(frequency.size)
  for f in range(frequency.size):
    if frequency[f] > -(fm2+5) and frequency[f]< -(fm1+5) or frequency[f] < (fm2+5) and frequency[f] > (fm1+5):
      filter[f] = 1

     
#output spectrum of 2nd message signal
  output_msg2_spectrum= transform_demodulated*np.array(filter)
  plt.subplot(6,2,8)
  plt.plot(frequency[:5000],(output_msg2_spectrum/N)[:5000])  
  plt.xlabel("frequency")
  plt.ylabel("amplitude")
  plt.title("output spectrum of 2nd message signal ")

#recovering the 2nd message signal fron its output spectrum
  output_msg2_wave=irfft(output_msg2_spectrum)
  plt.subplot(6,2,9)
  plt.plot(t[:2000],output_msg2_wave[:2000]) 
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("output 2nd message signal")

  # recovering the 1st message  signal 
  filter = [0]*(frequency.size)
  for f in range(frequency.size):
    if frequency[f] > -(fm1+5) and frequency[f]< -5 or frequency[f] < (fm1+5) and frequency[f] > 5:
      filter[f] = 1

   #output spectrum of 1st message signal
  output_msg1_spectrum =transform_demodulated*np.array(filter)   
  plt.subplot(6,2,10)
  plt.plot(frequency[:5000],(output_msg1_spectrum/N)[:5000])
  plt.xlabel("frequency")
  plt.ylabel("amplitude")
  plt.title("output spectrum of 1st message signal")

#recovering the 1st message signal fron its output spectrum
  output_msg1_wave=irfft(output_msg1_spectrum) 
  plt.subplot(6,2,11)
  plt.plot(t[:2000],output_msg1_wave[:2000])  
  plt.xlabel("time")
  plt.ylabel("amplitude")
  plt.title("output 1st message signal")

#input parameters
Ac=1       #carrier amplitude
fc=20000   #carrier freqency
Am1=0.3    # amplitde of the 1st message signal
fm1=1000   # freqency of the 1st message signal
Am2=0.8    # amplitde of the 2nd message signal
fm2=2000   # freqency of the 2nd message signal

am_modulation(Ac,Am1,Am2,fc,fm1,fm2)
  
plt.subplots_adjust(hspace=2)
plt.rc('font', size=8)
fig = plt.gcf()
fig.set_size_inches(16, 9)
plt.show()