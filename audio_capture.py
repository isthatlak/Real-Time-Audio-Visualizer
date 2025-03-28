import sounddevice as sd
import numpy as np
import scipy.fftpack

SAMPLE_RATE = 44100  # Audio sampling rate
DURATION = 3  # Recording duration in seconds

print("Recording...")
audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
sd.wait()  # Wait until recording is finished

print("Recording complete. Playing back...")
sd.play(audio_data, samplerate=SAMPLE_RATE)
sd.wait()