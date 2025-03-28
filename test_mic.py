import sounddevice as sd
import numpy as np

SAMPLE_RATE = 44100
DURATION = 3  # 3 seconds

print("Recording... Speak or play music now!")
audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
sd.wait()  # Wait until recording is finished

if np.max(audio_data) == 0:
    print("⚠️ No sound detected! Check your microphone.")
else:
    print("✅ Microphone is working! Sound detected.")