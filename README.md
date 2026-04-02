# 📈 Praktikum 6: Real-Time Analytics & Visualisasi Data Skala Besar
> Smart City: Mobilitas & Traffic (Decision-Oriented Dashboard)

---

## 📌 Gambaran Proyek
Repositori ini merupakan hasil pengerjaan **Praktikum 6** untuk mata kuliah **Big Data Technology**. Melanjutkan fondasi dari praktikum sebelumnya, proyek ini berfokus pada **Visualisasi Data Skala Besar (Large-Scale Streaming Visualization)**. 

Dengan mengambil *use case* **Smart City** (Monitoring kemacetan *real-time*, deteksi lonjakan *traffic*, dan analisis distribusi kendaraan) , sistem dioptimasi menggunakan teknik:
- **Window Aggregation:** Menyederhanakan data dengan agregasi waktu (per menit) agar visualisasi tetap ringan.
- **Data Downsampling:** Mengambil *subset* data terbaru agar proses *rendering* tidak *overload* .
- **Incremental Visualization:** Memperbarui data secara dinamis tanpa *lag* .

---

## 🛠️ Technology Stack
Teknologi yang digunakan mencerminkan arsitektur data *streaming* di industri:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3.10+** Bahasa utama untuk *generator* data, *analytics layer*, dan visualisasi *dashboard*.
- ![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat&logo=Apache%20Spark&logoColor=white) **PySpark (Structured Streaming)** *Engine* utama untuk memproses aliran data secara *real-time*.
- ![Parquet](https://img.shields.io/badge/Parquet-000000?style=flat&logo=apache&logoColor=white) **Apache Parquet** Format penyimpanan kolumnar (*Data Lake*) untuk efisiensi analitik cepat.
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas** *Library* untuk pemrosesan *Window Aggregation* (Resampling) dan perhitungan metrik.
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) **Streamlit** *Framework* untuk membangun *dashboard* analitik *real-time* yang interaktif.
- ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) **WSL (Ubuntu)** *Environment* pengembangan berbasis Linux untuk performa Big Data yang stabil.

---

## 📁 Struktur Direktori
Struktur *pipeline* dipisahkan secara modular berdasarkan domain untuk menjaga kerapian:

```text
bigdata-project-1/
├── alerts/                # Sistem peringatan otomatis
│   ├── __init__.py
│   └── transportation_alert.py
├── analytics/             # Layer analitik (Windowing, KPI, Pola)
│   ├── __init__.py
│   └── transportation_analytics.py
├── dashboard/             # Skrip visualisasi antarmuka (Big Data Optimized)
│   └── dashboard_transportation.py
├── data/
│   ├── checkpoints/       # Spark streaming checkpoints
│   └── serving/           # Serving layer (Output Parquet Data)
│       └── transportation/
├── scripts/               # Skrip logika utama
│   └── transportation/
│       ├── streaming_trip_layer.py
│       └── trip_generator.py
├── stream_data/           # Landing zone data mentah (JSON)
│   └── transportation/
├── .gitignore             
└── README.md              # Dokumentasi proyek
```

---

## ⚙️ Cara Menjalankan (How to Run)

Pastikan Virtual Environment sudah aktif, dan posisikan terminal di dalam direktori root project (~/bigdata-project-1). Jalankan 3 komponen ini di terminal terpisah dan harus berurutan :

### 1️⃣ Jalankan Trip Generator
Ketik di Terminal 1 (Jalankan pertama agar folder terbentuk):

```bash
python scripts/transportation/trip_generator.py
```

---

### 2️⃣ Jalankan Spark Streaming Engine
Ketik di Terminal 2:
```bash
spark-submit scripts/transportation/streaming_trip_layer.py
```

---

### 3️⃣ Jalankan Dashboard Streamlit
Ketik di Terminal 3:

```bash
streamlit run dashboard/dashboard_transportation.py
```


---

## 🎯 Tujuan Pembelajaran
Melalui praktikum ini, mahasiswa diharapkan mampu :

- Mengembangkan visualisasi real-time berbasis streaming data.
- Mengintegrasikan pipeline: Spark Streaming, Data Lake (Parquet), Dashboard (Streamlit).
- Membangun dashboard skala besar (large-scale visualization).
- Mengoptimalkan visualisasi agar tetap responsif pada data besar.
- Menghasilkan insight operasional real-time (decision-oriented).

---


## 👨‍💻 Author
Aisyahhhh :D
Dibuat untuk memenuhi tugas praktikum mata kuliah Big Data.

---

## ⭐ Catatan
"Dalam Big Data, visualisasi bukan hanya menampilkan data, tetapi mengubah data menjadi keputusan secara real-time."