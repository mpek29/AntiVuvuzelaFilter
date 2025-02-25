from scipy.io import wavfile
import matplotlib.pyplot as plt
import IPython.display as ipd
import numpy as np

path = "../wav/vuvuzela_only.wav"
Fs, data = wavfile.read(path)

spectrum, freqs, line = plt.magnitude_spectrum(data, Fs=Fs, color='C1')