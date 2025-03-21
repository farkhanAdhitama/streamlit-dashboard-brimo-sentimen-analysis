# Import library yang diperlukan
import streamlit as st
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Download data NLTK
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

# Load model dan vectorizer
model = joblib.load("random_forest_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Stemmer Bahasa Indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()


# Fungsi untuk membersihkan teks dari karakter yang tidak diperlukan
def delete_unused_char(text):
    text = re.sub(r"@[A-Za-z0-9]+", "", text)  # menghapus mention
    text = re.sub(r"#[A-Za-z0-9]+", "", text)  # menghapus hashtag
    text = re.sub(r"RT[\s]", "", text)  # menghapus RT
    text = re.sub(r"http\S+", "", text)  # menghapus link
    text = re.sub(r"[0-9]+", "", text)  # menghapus angka
    text = re.sub(r"[^\w\s]", "", text)  # menghapus karakter selain huruf dan angka
    text = text.replace("\n", " ")  # mengganti baris baru dengan spasi
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )  # menghapus semua tanda baca
    text = text.strip(" ")  # menghapus karakter spasi dari kiri dan kanan teks
    return text


# Fungsi untuk membersihkan teks
def cleaned_text(text):
    delete_unused_char(text)
    # 1. Lowercasing
    text = text.lower()
    # 2. Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # 3. Remove numbers
    text = re.sub(r"\d+", "", text)
    # 4. Tokenization
    words = word_tokenize(text)
    # 5. Remove stopwords
    stop_words = set(stopwords.words("indonesian"))  # Stopwords bahasa Indonesia
    words = [word for word in words if word not in stop_words]
    # 6. Ubah kate ke bentu asli dengan Stemmer  Sastrawi
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)


# Fungsi untuk prediksi sentimen
def predict_sentiment(text):
    text = cleaned_text(text)  # Preprocessing sebelum prediksi
    X = vectorizer.transform([text])  # Ubah teks menjadi vektor
    prediction = model.predict(X)[0]  # Prediksi sentimen
    return prediction


# Streamlit UI
st.title("Analisis Sentimen Review BRI Mobile 💳")
st.write("Masukkan review dan dapatkan prediksi sentimen (Positif, Negatif, Netral)")

# Input review dari pengguna
user_input = st.text_area("Masukkan review di sini:")

if st.button("Prediksi Sentimen"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu!")
    else:
        sentiment = predict_sentiment(user_input)
        st.success(f"Prediksi Sentimen: **{sentiment}**")
        # st.write(cleaned_text(user_input))

st.write("Dibuat dengan 💖 oleh Muhammad Farkhan Adhitama")
