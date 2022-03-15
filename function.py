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

write("train.wav", fs, wave.astype(np.init16))