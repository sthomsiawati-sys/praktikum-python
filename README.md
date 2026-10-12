# Praktikum Python: IDE, Virtual Environment, dan Git

## Deskripsi Proyek
Proyek ini merupakan tugas praktikum mata kuliah Pemrograman Berorientasi Objek (PBO) yang bertujuan untuk mempelajari dasar-dasar pemrograman Python menggunakan Visual Studio Code (VS Code), pengelolaan dependensi dengan virtual environment, serta pengelolaan versi kode menggunakan Git dan GitHub.

Proyek ini memiliki dua program utama:

- **`halo.py`**: Program Python sederhana yang meminta nama pengguna dan menampilkan pesan sapaan.
- **`tampil.py`**: Program yang menggunakan library `rich` untuk menampilkan tabel daftar alat praktikum di terminal.

Proyek ini juga menggunakan `requirements.txt` untuk menyimpan daftar dependensi yang dibutuhkan agar program dapat dijalankan kembali di komputer lain.

## Teknologi yang Digunakan
- Python versi 3.10 atau lebih baru.
- Visual Studio Code (VS Code) sebagai IDE.
- Virtual environment (`venv`) untuk mengisolasi dependensi proyek.
- pip untuk menginstal paket Python.
- Library `rich` untuk mempercantik tampilan terminal.
- Git untuk mencatat riwayat perubahan kode.
- GitHub untuk menyimpan repositori secara online.

## Membuat Virtual Environment
Virtual environment digunakan untuk memisahkan paket yang dibutuhkan oleh proyek ini dari proyek Python lainnya.

Pastikan terminal berada di dalam folder `praktikum-python`.

**Windows:**
py -m venv .venv
Alternatifnya:
python -m venv .venv

**macOS atau Linux:**
python3 -m venv .venv

Setelah perintah berhasil dijalankan, folder `.venv` akan dibuat di dalam folder proyek.

## Mengaktifkan Virtual Environment
Aktifkan virtual environment sesuai sistem operasi yang digunakan.

**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```
**Windows Command Prompt (CMD):**
```bat
.venv\Scripts\activate.bat
```
**macOS atau Linux:**
```bash
source .venv/bin/activate
```

Jika berhasil, terminal akan menampilkan tanda `(.venv)` di awal baris perintah.

Untuk memastikan environment yang aktif sudah benar, jalankan:

```bash
python -c "import sys; print(sys.prefix)"
```

Lokasi yang ditampilkan seharusnya berada di dalam folder `.venv` proyek.

Untuk menonaktifkan virtual environment, gunakan:

```bash
deactivate
```

## Menginstal Dependensi
Pastikan virtual environment sudah aktif sebelum menginstal paket.
Untuk menginstal library `rich`, jalankan:
python -m pip install rich

Periksa paket yang sudah terinstal dengan perintah:
pip list

Simpan daftar dependensi ke dalam file `requirements.txt` menggunakan:
pip freeze > requirements.txt

File `requirements.txt` akan berisi nama paket beserta versinya.

Jika virtual environment dibuat ulang atau proyek dipindahkan ke komputer lain, instal kembali semua dependensi dengan:
pip install -r requirements.txt

## Menjalankan Program

### A. Menjalankan `halo.py`

Program ini meminta nama pengguna dan menampilkan pesan sapaan.

Jalankan perintah berikut di terminal:

```bash
python halo.py
```

Pada Windows, kamu juga dapat menggunakan:

```bash
py halo.py
```

Contoh keluaran program:

```text
Masukkan nama Anda: Siti Homsiawati
Halo, Siti Homsiawati! Selamat datang di praktikum Python.
```

### B. Menjalankan `tampil.py`

Program ini menggunakan library `rich` untuk menampilkan tabel daftar alat praktikum.

Jalankan perintah berikut:

```bash
python tampil.py
```

Program akan menampilkan tabel dengan kolom nomor, alat, dan fungsi, yang berisi informasi tentang VS Code, virtual environment, dan Git.

Pastikan library `rich` sudah terinstal di virtual environment sebelum menjalankan program ini.

##  Kesimpulan

Melalui proyek praktikum ini, mahasiswa mempelajari cara membuat dan menjalankan program Python, mengelola dependensi menggunakan virtual environment dan pip, serta mendokumentasikan proyek dengan README.md.

Penggunaan Git dan GitHub juga membantu mencatat perubahan kode, menyimpan riwayat commit, dan mengunggah proyek ke repositori online agar lebih mudah dikelola dan dikembangkan.

