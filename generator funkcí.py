import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate = 44100
f = 50   #Hz

t = np.arange(0,1,1/sample_rate)  #Time


#normalize function
def norm(data):
    min_v = min(data)
    max_v = max(data)
    return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1


####PRODUCE SIGNALS
signal = np.sin(2*np.pi*f*t)      #Sinus
#signal = np.cos(2*np.pi*f*t)       #Cosinus
#signal = (np.mod(f*t,1) < 0.5)*2.0-1 #Rectangle


noise = np.random.randn(*signal.shape)

####COMBINE NOISE AND SIGNAL
dirty =  norm(signal+noise)

####WRITE AUDIO FILE
signal = signal * 32767
signal = np.int16(signal)
wavfile.write("file.wav", sample_rate, signal)

####PLOT SIGNAL####
plt.plot(t, signal,"black")
plt.plot(t, signal+noise,"blue");
plt.ylabel("napětí[V]")
plt.xlabel("čas[s]")
plt.title("Signál")
plt.show()
