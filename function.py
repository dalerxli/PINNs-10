import numpy as np
import scipy.io
from math import sin, cos, exp
from scipy.io.wavfile import read, write

def get_sine_wave(frequency_hz, length_s=0.5, sample_rate_hz=16000):
    # create time vector $t$
    time_points = np.linspace(0, length_s,
                              int(length_s * sample_rate_hz),
                              endpoint=False)
    # return sinus of frequency $f$, i.e. variable frequency_hz
    return np.sin(2 * np.pi * frequency_hz * time_points) 

fs = 16000               # Sampling frequency
# Formant freqnecy: a
formant = [740,1180,2640] # f1, f2, f3
wave =0
for i in formant:
    wave += get_sine_wave(i)

write("Data/train.wav", fs, wave.astype(np.int16))
fs, gold = read("Data/aa_DR1_MCPM0_sa1.wav")
gold = gold.reshape(157,10)
# Save samples as x to MATLIB 
x = np.linspace(-1, 1, num=157, dtype=float)
t = np.linspace(0, 0, num=10, dtype=int)
scipy.io.savemat('Data/sound.mat', mdict={'x':x, 't':t, 'usol': gold}, oned_as='column')


