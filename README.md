# 🍃 Praktikum 5: Big Data Analytics & Use Case
> Decision-Oriented System (Industrial Style - Multi-Domain Pipeline: Smart Transportation)

---

## 📌 Gambaran Proyek
Repositori ini merupakan hasil pengerjaan **Praktikum 5** untuk mata kuliah **Big Data Technology**. [cite_start]Fokus utama proyek ini adalah memperluas arsitektur data dengan menambahkan domain baru, yaitu **Smart Transportation** [cite: 33-34]. 

Proyek ini tidak hanya sekadar mengolah dan menampilkan data, tetapi telah di- *upgrade* menjadi **Decision-Oriented System** yang mampu:
- [cite_start]Menghasilkan *insight* secara *real-time*[cite: 24, 59].
- [cite_start]Memberikan peringatan (*alert*) otomatis berdasarkan kondisi data[cite: 25, 60].
- [cite_start]Mendukung pengambilan keputusan operasional, taktis, dan strategis dengan cepat[cite: 26, 716].

---

## 🛠️ Technology Stack
Teknologi yang digunakan mencerminkan arsitektur data *streaming* di industri:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3.10+** Bahasa utama untuk *generator* data, *analytics layer*, dan visualisasi *dashboard*.
- [cite_start]![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat&logo=Apache%20Spark&logoColor=white) **PySpark (Structured Streaming)** *Engine* utama untuk memproses aliran data secara *real-time*[cite: 49].
- [cite_start]![Parquet](https://img.shields.io/badge/Parquet-000000?style=flat&logo=apache&logoColor=white) **Apache Parquet** Format penyimpanan kolumnar (*Data Lake*) untuk efisiensi analitik cepat [cite: 50-51].
- [cite_start]![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas** *Library* untuk pemrosesan dan perhitungan metrik analitik (*Analytics Engine*)[cite: 139].
- [cite_start]![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) **Streamlit** *Framework* untuk membangun *dashboard* analitik *real-time* yang interaktif[cite: 230].
- ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) **WSL (Ubuntu)** *Environment* pengembangan berbasis Linux untuk performa Big Data yang stabil.

---

## 📁 Struktur Direktori
[cite_start]Struktur *pipeline* dipisahkan secara modular berdasarkan domain untuk menjaga kerapian [cite: 62-64]:

```text
bigdata-project-1/
├── alerts/                # Sistem peringatan otomatis
│   ├── __init__.py
│   └── transportation_alert.py
├── analytics/             # Layer analitik (Agregasi, KPI, Pola)
│   ├── __init__.py
│   └── transportation_analytics.py
├── dashboard/             # Skrip visualisasi antarmuka
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

### 1️⃣ Jalankan Spark Streaming Engine
Ketik di Terminal 1:

```bash
spark-submit scripts/transportation/streaming_trip_layer.py
```

---

### 2️⃣ Jalankan Trip Generator
Ketik di Terminal 2:
```bash
python scripts/transportation/trip_generator.py
```

---

### 3️⃣ Jalankan Dashboard Streamlit
Ketik di Terminal 3:

```bash
streamlit run dashboard/dashboard_transportation.py
```


---

## 🎯 Tujuan Pembelajaran
Melalui praktikum ini, mahasiswa diharapkan memahami:

- Mengembangkan sistem Big Data Analytics berbasis streaming.
- Membangun Decision-Oriented System (Insight + Alert).
- Mengelola multi-domain data pipeline.
- Mengintegrasikan data ingestion, streaming processing, analytics layer, dan dashboard.

---


## 👨‍💻 Author
Aisyahhhh :D
Dibuat untuk memenuhi tugas praktikum mata kuliah Big Data.

---

## ⭐ Catatan
