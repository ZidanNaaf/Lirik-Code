import time
import os
import sys

lyrics = [
    "Kari Manis",
    "kurang manis",
    "tambahi",
    "gulo",
]

os.system('cls' if os.name == 'nt' else 'clear')

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)  # Efek ketik
    print()
    time.sleep(1)
