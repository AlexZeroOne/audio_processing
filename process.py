import librosa
import soundfile as sf
import matplotlib.pyplot as plt

def makeUint8(values):
    result = []
    for i in range(len(values)):
        result.append(int((values[i] + 1) * 127.5))
    return result

def saveTextFile(values, filenale):
    with open(filenale, 'w') as f:
        f.write('{')
        for i in range(len(values)):
            f.write(str(values[i]) + ', ')
        f.write('}')

y, sr = librosa.load('BabyElephantWalk60.wav', sr=22050)
y_6k = librosa.resample(y, orig_sr=sr, target_sr=6000)
#sf.write('BabyElephantWalk60_6k.wav', y_6k, 6000, 'PCM_U8')

y_6k_255 = makeUint8(y_6k)
print(len(y_6k_255))
saveTextFile(y_6k_255, 'BabyElephantWalk60_6k_255.dat')

# plt.subplot(3, 1, 1)
# plt.plot(y, label = 'y')
# plt.grid()

# plt.subplot(3, 1, 2)
# plt.plot(y_6k, label = 'y_6k')
# plt.grid()

# plt.subplot(3, 1, 3)
# plt.plot(y_6k_255, label = 'y_6k_255')
# plt.grid()

# plt.show()

print("done")
