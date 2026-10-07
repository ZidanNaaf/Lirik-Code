import time
import os
import sys

lyrics = [
    "Aduh abang bukan maksudku begitu",
    "Masalah stecu bukan brarti tak mau",
    "Jual mahal dikit kan bisa",
    "Coba kase effortnya saja",
    "Kalo memang cocok bisa datang ke rumah",
    ".",
    "Stecu stecu stelan cuek baru malu",
    "Adu ade ini mau juga abang yang rayu",
    "Stecu stecu stelan cuek baru malu",
    "Adu ade ini mau juga abang yang maju",
]

os.system('cls' if os.name == 'nt' else 'clear')

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)  # Efek ketik
    print()
    time.sleep(0.7)
