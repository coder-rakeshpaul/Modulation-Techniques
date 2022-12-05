
import numpy as np
from numpy import cos , pi , linspace
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft , fftfreq , ifft

class FSK:
  def __init__(self,vc,fm,b,fs):
    self.vc = vc
    self.fm =fm
    self.b = b
    self.len_b = fs/len(str(b))
    self.fs = fs
    self.t = linspace(0,1,fs)

# generating the carrier signal
  def carrier_signal(self,d):
    v= self.vc * cos(2*pi*(self.fm * d)*self.t)
    return v

# generating the bit wave
  def bit_wave(self):
    c=[]
    b = str(self.b)
    for i in b:
      for j in range(int(self.len_b)):
        c.append(int(i))
    return np.array(c)    

# generating the FSK signal
  def modulated_signal(self):
    d=[]
    for i in self.bit_wave():
      if (i==1):
        d.append(0.5)
      else:
        d.append(1)  
    return self.carrier_signal(np.array(d))
    
# generating the spectrum of the FSK signal
  def spectrum(self):
    return fft(self.modulated_signal())    

B=1001 # input bits
a = FSK(vc=10 ,fm=100, b=B, fs=60000) # input parameters 

# plottimg the signals
fig , ax = plt.subplots(4,1)
bit_wave, = ax[0].plot(a.t,a.bit_wave())
carrier_signal, = ax[1].plot(a.t,a.carrier_signal(d=1))
modulated_signal, = ax[2].plot(a.t,a.modulated_signal())
spectrum, = ax[3].plot(fftfreq(a.fs,1/a.fs),np.abs(a.spectrum())/a.fs)
ax[3].set_xlim(-100,100)

ax[0].set_xlabel('time')
ax[0].set_ylabel('Amplitude')
ax[1].set_xlabel('time')
ax[1].set_ylabel('Amplitude')
ax[2].set_xlabel('time')
ax[2].set_ylabel('Amplitude')
ax[3].set_xlabel('Freqency')
ax[3].set_ylabel('Amplitude')
ax[0].set_title(' bit wave')
ax[1].set_title(' carrier wave')
ax[2].set_title(' FSK wave')
ax[3].set_title('spectrum')



plt.subplots_adjust(hspace=0.5)
plt.rc('font', size=12)
fig = plt.gcf()
fig.set_size_inches(16, 12)
plt.show()