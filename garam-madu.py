import time
import os
import sys

lyrics = [
    "Garam dan madu, rasa di dadaku",
    "Manis menyakitkan, cinta yang membingungkan",
    "Langkah kita tak seirama",
    "Namun hati tetap ingin bersama"
]

os.system('cls' if os.name == 'nt' else 'clear')

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Efek ketik
    print()
    time.sleep(1.5)
