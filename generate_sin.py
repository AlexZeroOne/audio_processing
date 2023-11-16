import math
import struct
import wave
import matplotlib.pyplot as plt

samplerate = 6000
left_channel = [0.5 * math.sin(10 * math.pi * 440.0 * i / samplerate) for i in range(samplerate * 5)]
right_channel = left_channel

with wave.open("sound2.wav", "w") as f:
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(samplerate)
    for samples in zip(left_channel, right_channel):
        for sample in samples:
            sample = int(sample * (2 ** 15 - 1))
            f.writeframes(struct.pack("<h", sample))

# plt.plot(left_channel, label = 'left_channel')
# plt.legend()
# plt.show()

print("done")
