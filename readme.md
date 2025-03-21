# Analisis Sentimen Review BRI Mobile 💳

Proyek ini adalah aplikasi web untuk analisis sentimen review BRI Mobile menggunakan Streamlit. Aplikasi ini memprediksi sentimen (Positif, Negatif, Netral) dari review yang diberikan oleh pengguna.

## Fitur

- Membersihkan teks dari karakter yang tidak diperlukan
- Mengubah teks menjadi huruf kecil
- Menghapus tanda baca dan angka
- Tokenisasi teks
- Menghapus stopwords bahasa Indonesia
- Stemming kata-kata menggunakan Stemmer Sastrawi
- Prediksi sentimen menggunakan model Random Forest

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/farkhanAdhitama/streamlit-brimo-sentimen-analysis.git
   cd streamlit-brimo-sentimen-analysis
   ```

2. Buat virtual environment dan aktifkan:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Untuk Windows
   # source venv/bin/activate  # Untuk macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Download data NLTK yang diperlukan:

   ```python
   import nltk
   nltk.download("stopwords")
   nltk.download("punkt")
   nltk.download("punkt_tab")
   ```

5. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

## Penggunaan

1. Buka aplikasi di browser Anda.
2. Masukkan review pada area teks yang disediakan.
3. Klik tombol "Prediksi Sentimen".
4. Lihat hasil prediksi sentimen.

## Struktur Proyek

- `app.py`: File utama yang berisi kode aplikasi Streamlit.
- `random_forest_model.pkl`: Model Random Forest yang telah dilatih.
- `tfidf_vectorizer.pkl`: Vectorizer TF-IDF yang telah dilatih.

## Note

Direkomendasikan menggunakan virtual environment untuk menjalankan project

## Streamlit App

```
https://farkhanadhitama-streamlit-dashboard-brimo-sentimen-a-app-whenzn.streamlit.app
```

## Kontributor

Dibuat dengan 💖 oleh Muhammad Farkhan Adhitama
