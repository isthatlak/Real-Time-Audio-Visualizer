import pygame
import numpy as np
import sounddevice as sd
import scipy.fftpack

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Audio settings
SAMPLE_RATE = 44100
fft_magnitudes = np.zeros(50)  # Placeholder for FFT data

# ✅ Debugging: Check FFT values
def audio_callback(indata, frames, time, status):
    global fft_magnitudes
    if status:
        print("SoundDevice Status Error:", status)

    # Compute FFT (Fast Fourier Transform)
    fft_result = scipy.fftpack.fft(indata[:, 0])
    fft_magnitudes = np.abs(fft_result[:50])  # Get the first 50 frequency bands

    # ✅ Print FFT values to check if they are updating
    print("FFT Magnitudes:", fft_magnitudes)

# Start real-time audio stream
stream = stream = sd.InputStream(device=1, callback=audio_callback, samplerate=SAMPLE_RATE, channels=2)
stream.start()

running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    # ✅ Debug: Check FFT values
    print("FFT Data (before scaling):", fft_magnitudes)

    # 🎵 **Bar Visualization**
    for i, magnitude in enumerate(fft_magnitudes):
        bar_height = int(magnitude * (i + 1) * 2)  # Scale height dynamically
        color = (i * 5, 255 - i * 5, 255)  # Color gradient from blue to red
        pygame.draw.rect(screen, color, (i * 15, HEIGHT - bar_height, 10, bar_height))

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

stream.stop()
pygame.quit()