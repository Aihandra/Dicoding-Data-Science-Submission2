# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan edutech ini memiliki tujuan utama untuk meningkatkan angka kelulusan mahasiswa dan menurunkan angka dropout. Data historis mahasiswa digunakan untuk memahami pola dan faktor-faktor yang berkontribusi terhadap status akhir mahasiswa, apakah mereka dropout, lulus, atau masih aktif (enrolled).

### Permasalahan Bisnis

- Tingginya angka mahasiswa dropout (32,1%) yang berdampak pada efektivitas dan efisiensi sistem pendidikan tinggi.
- Perusahaan kesulitan mengidentifikasi mahasiswa yang berpotensi dropout secara dini.
- Perlunya pemahaman mendalam mengenai faktor-faktor yang mempengaruhi kelulusan mahasiswa.

### Cakupan Proyek

- Menganalisis data historis mahasiswa untuk memahami komposisi status mereka.
- Membangun model machine learning untuk memprediksi status akhir mahasiswa (graduate, dropout, enrolled).
- Membangun dashboard bisnis interaktif sebagai alat bantu visualisasi untuk pengambilan keputusan manajemen.
- Memberikan rekomendasi berbasis data untuk mengurangi angka dropout dan meningkatkan kelulusan.

### Persiapan

**Sumber data:**

- Dataset: [students_performance.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv). Dataset "Students' Performance" berisi informasi dari mahasiswa program sarjana yang mencakup aspek akademik, demografis, sosial ekonomi, dan performa mereka di semester pertama dan kedua.

Berikut beberapa fitur penting:

                    | Fitur | Deskripsi |
                    |------|-----------|
                    | `Marital status` | Status pernikahan mahasiswa |
                    | `Application mode` | Jalur pendaftaran mahasiswa |
                    | `Application order` | Urutan pilihan jurusan saat mendaftar |
                    | `Course` | Program studi yang diambil |
                    | `Daytime/evening attendance` | Apakah kuliah siang atau malam |
                    | `Previous qualification` | Kualifikasi sebelum masuk perguruan tinggi |
                    | `Previous qualification (grade)` | Nilai akhir dari pendidikan sebelumnya |
                    | `Nationality` | Kewarganegaraan |
                    | `Mother's qualification` | Tingkat pendidikan ibu |
                    | `Father's qualification` | Tingkat pendidikan ayah |
                    | `Mother's occupation` | Pekerjaan ibu |
                    | `Father's occupation` | Pekerjaan ayah |
                    | `Admission grade` | Nilai masuk (0-200) |
                    | `Displaced` | Apakah mahasiswa berasal dari luar kota |
                    | `Educational special needs` | Apakah memiliki kebutuhan pendidikan khusus |
                    | `Debtor` | Apakah mahasiswa memiliki tunggakan |
                    | `Tuition fees up to date` | Status pembayaran biaya kuliah |
                    | `Gender` | Jenis kelamin |
                    | `Scholarship holder` | Apakah penerima beasiswa |
                    | `Age at enrollment` | Usia saat pendaftaran |
                    | `International` | Mahasiswa internasional |
                    | `Curricular units 1st sem (credited)` | Unit yang dikonversi dari studi sebelumnya |
                    | `Curricular units 1st sem (enrolled)` | Unit yang diambil di semester 1 |
                    | `Curricular units 1st sem (evaluations)` | Jumlah evaluasi semester 1 |
                    | `Curricular units 1st sem (approved)` | Unit yang lulus di semester 1 |

                    Untuk deskripsi lengkap semua fitur (https://archive.ics.uci.edu/dataset/697/higher+education+students+performance+evaluation).

**Setup environment:**

```bash
pip install -r requirements.txt
```

## Business Dashboard

Dashboard dikembangkan menggunakan **Looker Studio** untuk memvisualisasikan pola dan tren dari data mahasiswa, termasuk faktor-faktor yang memengaruhi keberhasilan atau kegagalan studi.

**Dashboard mencakup:**

- Distribusi status mahasiswa (Graduate, Dropout, Enrolled).
- Korelasi antara fitur demografis dan status akhir mahasiswa.
- Rata-rata nilai masuk dan usia berdasarkan status.
- Komposisi jurusan dan jalur masuk yang dominan di masing-masing status.
- Insight spesifik seperti hubungan antara pekerjaan orang tua, latar belakang pendidikan, dan kelulusan mahasiswa.

 [Akses Dashboard Looker Studio](https://lookerstudio.google.com/reporting/b4ce98e2-dd81-420e-b61f-1a06404aba42/page/jxZOF)

## Menjalankan Sistem Machine Learning

Sistem machine learning berupa aplikasi prediksi status mahasiswa berbasis **Streamlit**. Model telah dilatih dan disimpan sebagai `.pkl`.

**Langkah menjalankan aplikasi:**

1. Pastikan semua dependensi telah diinstal.
2. Jalankan aplikasi:

```bash
streamlit run app.py
```

Aplikasi akan menampilkan form input berdasarkan fitur yang dipilih (`selected_features`) dan memberikan prediksi status mahasiswa (Graduate / Dropout / Enrolled).

Aplikasi ini ditujukan sebagai **prototype sistem pendukung keputusan** bagi staf akademik untuk mengidentifikasi risiko dropout sejak awal.

## Conclusion

Proyek ini membuktikan bahwa data akademik dan sosial mahasiswa dapat digunakan secara efektif untuk memprediksi risiko dropout. Model klasifikasi yang dibangun mampu menghasilkan prediksi dengan akurasi baik, dan dashboard memberikan insight strategis yang bermanfaat untuk pengambilan keputusan di tingkat institusi pendidikan.

Dengan sistem ini, institusi dapat:

- Menyusun kebijakan preventif terhadap risiko dropout.
- Memberikan dukungan personalisasi kepada mahasiswa.
- Meningkatkan tingkat kelulusan melalui pemanfaatan data.

## Rekomendasi Action Items

- Membangun sistem monitoring internal yang mengawasi kinerja mahasiswa secara berkala, khususnya di semester 1.
- Mengintegrasikan sistem prediksi ini ke dalam sistem informasi akademik untuk real-time analysis.
- Memberikan perhatian lebih pada mahasiswa dengan latar belakang pendidikan dan ekonomi rendah, termasuk beasiswa dan mentoring.
- Membuat program bimbingan akademik khusus untuk mahasiswa dengan nilai masuk rendah atau keterlambatan pembayaran.
- Menggunakan hasil prediksi untuk menyusun intervensi berbasis data seperti konseling, penyesuaian beban studi, atau modifikasi kurikulum.


---
