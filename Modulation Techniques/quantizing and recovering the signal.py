
import numpy as np
from numpy import pi, cos
import matplotlib.pyplot as plt
from scipy.fft import fft , ifft, fftfreq
import pandas as pd

vm = 10     # amplitude of the sinal
fm =3000    # frequency of the signal
fs = 20*fm  # sampling frequency
n=3         # number of bits
L = 2**n    # number of levels
step_size = 20/L  # step size

t= np.linspace(0,1,fs) # time duration
v = vm*cos(2*pi*fm*t)  # input signal
v_shifted = v +10      # shifted signal 

q_levels= np.array([i for i in range(L)] ) * step_size # Quantizing the signal

# generting the quantized signal
q_signal = np.zeros(v.size) 
for i in range(v.size):
  for k in q_levels:
    if ((v_shifted[i] >= k ) and (v_shifted[i]< k+ step_size)):
        q_signal[i] = k

# mapping the signal
def encoding(q_levels):
  encoded_levels=[bin(int(q))[2:] for q in range(q_levels.size)]

  mapped_levels = dict(zip(encoded_levels,q_levels))
  return mapped_levels 

# getting the spectrum of the Quantized siganl
freq = fftfreq(fs,1/fs)
spectrum = fft(q_signal)

# recovering the original signal
filter = [0]*(freq.size)
for f in range(freq.size):
  if freq[f] > -(fm+50) and freq[f] < (fm+50):
     filter[f] = 1
final_spectrm = filter * spectrum
recovered_signal = ifft(final_spectrm)

encoded = encoding(q_levels)
data = {'encoding':encoded.keys(),
        'value': encoded.values()
        }
df= pd.DataFrame(data)
df = df.reset_index(drop=True)
print(df)

# plotting the waveforms
fig, ax = plt.subplots(4,1)
original_shifted_signal, = ax[0].plot(t,v_shifted)
quantized_siganl, = ax[0].step(t, q_signal)
ax[0].set_xlim(0,0.001)
ax[0].set_xlabel("time")
ax[0].set_ylabel("Amplitude")
ax[0].legend([original_shifted_signal,quantized_siganl],['input','Quantized'],loc=4)

recovered_signal_spectrum, = ax[1].plot(freq,np.abs(final_spectrm)/fs)
ax[1].set_xlabel("frequency")
ax[1].set_ylabel("Amplitude")

recovered_signal_plot, = ax[2].plot(t,recovered_signal)
quantized_siganl, = ax[2].step(t, q_signal)
ax[2].set_xlabel("time")
ax[2].set_ylabel("Amplitude")
ax[2].legend([recovered_signal_plot,quantized_siganl],['recovered','Quantized'],loc =4)
ax[2].set_xlim(0,0.001)

original_shifted_signal, = ax[3].plot(t,v_shifted)
recovered_signal_plot, = ax[3].plot(t,recovered_signal)
ax[3].set_xlim(0,0.001)
ax[3].set_xlabel("time")
ax[3].set_ylabel("Amplitude")
ax[3].legend([original_shifted_signal,recovered_signal_plot],['input','recovered'],loc=4)




plt.subplots_adjust(hspace=0.5)
plt.rc('font', size=12)
fig = plt.gcf()
fig.set_size_inches(16, 12)
plt.show()