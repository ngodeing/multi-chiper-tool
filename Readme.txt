#Multi Cipher Tool

Halo, selamat datang di Multi Cipher Tool! Ini adalah program yang bisa kamu pakai untuk enkripsi dan dekripsi teks dengan tiga metode: Vigenere, Playfair, dan Hill.

## Cara Menggunakan Program

1. **Persiapan**:
   - Pastikan kamu sudah install Python dan Flask di laptop/PC kamu.
   - Kalau belum, kamu bisa install Flask pakai perintah berikut:
     ```
     pip install Flask
     ```

2. **Menjalankan Program**:
   - Setelah semua terinstal, jalankan aplikasi dengan perintah ini:
     ```
     python app.py
     ```
   - Aplikasi bakal jalan di localhost, biasanya di `http://127.0.0.1:5000/`.

3. **Menggunakan Antarmuka**:
   - Buka browser kamu dan akses alamat itu.
   - Di halaman utama, kamu bakal lihat form buat milih jenis cipher dan masukin teks.

4. **Memilih Cipher**:
   - Pilih jenis cipher yang mau kamu pakai dari dropdown (Vigenere, Playfair, atau Hill).

5. **Masukkan Teks**:
   - Kamu bisa masukin plaintext atau ciphertext di kolom "Plaintext / Ciphertext". Atau, kamu bisa unggah file teks (.txt) yang berisi teks yang mau diproses.

6. **Masukkan Kunci**:
   - Masukin kunci yang kamu mau untuk enkripsi atau dekripsi. Ingat, kunci ini harus minimal 12 karakter, ya!

7. **Memilih Operasi**:
   - Pilih apakah kamu mau mengenkripsi atau mendekripsi teks dengan memilih opsi yang sesuai.

8. **Menjalankan Proses**:
   - Klik tombol "Proses" untuk mulai. Hasil enkripsi atau dekripsi bakal muncul di bawah form.

9. **Pesan Kesalahan**:
   - Kalau kunci kurang dari 12 karakter atau kamu nggak masukin teks, bakal ada pesan kesalahan yang muncul buat bantu kamu.

## Catatan Tambahan
- Pastikan file yang kamu unggah adalah file teks (.txt) dan nggak kosong.
- Kamu bisa pakai kombinasi input teks dan file, tapi nggak perlu isi keduanya.

Terima kasih sudah pakai Multi Cipher Tool! Kalau ada pertanyaan atau saran, jangan ragu untuk hubungi pengembangnya.
