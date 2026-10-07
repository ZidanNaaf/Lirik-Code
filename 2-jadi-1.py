import time
import os
import sys

lyrics = [
    "Ku merasakan apa yang kau rasakan",
    "Tanpa ragu kubilang kamu yang paling paham aku",
    "Dua jadi Satu",
    "Belah hati aku",
    "Aku mau maju "
    "Tapi tinggal tunggu waktu",
    "Ku merasakan apa yang kau rasakan",
    "Tanpa ragu kubilang kamu yang paling paham aku",
    "Dua jadi Satu",
    "Belah hati aku",
    "Aku mau maju "
    "Tapi tinggal tunggu waktu",
]

os.system('cls' if os.name == 'nt' else 'clear')

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)  # Efek ketik
    print()
    time.sleep(0.55)
