import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

audio_file = r"E:\hello.mp3"
sample_rate, audio_data = wavfile.read(audio_file)

fft_result = np.fft.fft(audio_data)
fft_freqs = np.fft.fftfreq(len(fft_result), 1.0 / sample_rate)

magnitude = np.abs(fft_result)

plt.figure(figsize=(10,6))
plt.plot(fft_freqs, magnitude)
plt.xlabel('频率')
plt.ylabel('振幅')
plt.title('傅里叶变换结果')
plt.grid(True)
plt.show()

