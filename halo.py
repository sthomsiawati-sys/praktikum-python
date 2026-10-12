# halo.py - program Python pertama
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

nama = input("Masukkan nama Anda: ")
print(Fore.GREEN + f"Halo, {nama}! Selamat datang di praktikum Python.")

try:
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    tahun_sekarang = 2026
    perkiraan_usia = tahun_sekarang - tahun_lahir
    print(Fore.CYAN + f"Perkiraan usia Anda tahun ini adalah {perkiraan_usia} tahun.")
except ValueError:
    print(Fore.RED + "Input tidak valid! Harap masukkan angka untuk tahun lahir.")

print(Fore.YELLOW + "Semoga sukses!")