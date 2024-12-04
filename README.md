# Reccomendation System

## Project Overview
Sistem rekomendasi film sangat penting di platform di mana pengguna dihadapkan pada banyak pilihan konten. Pengguna sering kesulitan menemukan konten yang sesuai dengan selera mereka, yang dapat mengakibatkan pengalaman pengguna yang kurang baik dan ketidakpuasan. Tantangannya adalah bagaimana menyaring konten yang sangat banyak dan memberikan rekomendasi yang personal untuk meningkatkan keterlibatan dan kepuasan pengguna dengan platform tersebut.

Proyek ini bertujuan untuk membangun sistem rekomendasi yang membantu pengguna menemukan film yang sesuai dengan preferensi mereka di antara banyaknya pilihan yang tersedia. Sistem rekomendasi ini menggunakan teknik analisis data dan machine learning untuk memberikan rekomendasi yang dipersonalisasi. Fokus dari proyek ini adalah mengembangkan sistem rekomendasi film menggunakan metode collaborative filtering berdasarkan kesamaan konten dan perilaku pengguna.

## Business Understanding
Problem Statements:
Pengguna sering mengalami kesulitan dalam menemukan film yang sesuai dengan preferensi mereka di antara banyaknya pilihan yang tersedia. Hal ini dapat menyebabkan pengalaman pengguna yang buruk dan ketidakpuasan terhadap platform streaming.
Goals:
- Mengembangkan sistem rekomendasi film yang dapat memberikan saran film kepada pengguna berdasarkan rating dan preferensi mereka.
- Meningkatkan kepuasan pengguna dengan menyediakan rekomendasi film yang relevan dan sesuai dengan minat mereka.
- Mengukur efektivitas sistem rekomendasi menggunakan metrik evaluasi yang sesuai.

## Data Understanding
Dataset yang digunakan dalam proyek ini terdiri dari dua file:

- movies.csv: Menyediakan informasi mengenai film, termasuk ID film, judul, dan genre. Dataset tersebut memiliki 27279 data
- ratings.csv: Berisi informasi tentang rating yang diberikan pengguna kepada film. Dataset tersebut memiliki 1048576 data

Data yang digunakan hanya sebagian dari dataset penuh, yaitu top 20.000 data, untuk mempercepat proses perhitungan dan pemodelan.

Kondisi Data: Data sudah dibersihkan dan tidak ada nilai yang hilang setelah penggabungan.
Link Sumber Data: https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset?select=rating.csv
- Variabel/Fitur dalam Data:
	- movies.csv
	movieId: ID unik untuk setiap film.
	title: Judul film.
	genres: Genre film yang terdaftar.

	- ratings.csv
	userId: ID unik untuk setiap pengguna.
	movieId: ID film yang di-rating.
	rating: Rating yang diberikan oleh pengguna (skala 1-5).
	timestamp: Waktu saat rating diberikan.

## Data Preparation
Dalam tahap ini, beberapa teknik data preparation yang diterapkan adalah:

- Penggabungan Dataset: Menggunakan pd.merge() untuk menggabungkan ratings dan movies berdasarkan movieId.
- Pivot Table: Membuat pivot table menggunakan pd.pivot_table() untuk mengubah data menjadi format yang lebih mudah digunakan untuk analisis.
- Penanganan Missing Values: Menggunakan fillna(0) untuk mengganti nilai yang hilang dengan 0, menunjukkan bahwa pengguna belum memberikan rating untuk film tertentu.

## Modeling and Result
Model yang digunakan dalam sistem rekomendasi ini adalah cosine similarity, yang berfungsi untuk mengukur seberapa mirip dua film berdasarkan rating yang diberikan oleh pengguna. Jika dua film memiliki pola rating yang serupa, maka nilai cosine similarity-nya akan tinggi, sehingga film tersebut dianggap mirip.

Cara Kerjanya:

- Representasi Vektor:
Objek (dalam hal ini film) diwakili oleh vektor. Setiap vektor berisi informasi, seperti rating yang diberikan pengguna.

- Menghitung Sudut:
Cosine similarity mengukur sudut antara dua vektor, bukan perbedaan nilai mereka. Rumus cosine similarity adalah:

Cosine Similarity = 𝐴 ⋅ 𝐵 / ∣∣𝐴∣∣ ⋅ ∣∣B∣∣

Di mana:

A dan B adalah vektor film

𝐴 ⋅ 𝐵 adalah hasil perkalian dot product dari kedua vektor

∣∣𝐴∣∣ ⋅ ∣∣B∣∣ adalah hasil perkalian panjang (norma) kedua vektor

- Nilai Cosine Similarity:

Jika nilainya 1, berarti kedua vektor sepenuhnya mirip.

Jika nilainya 0, berarti tidak ada kemiripan.

Nilai berkisar antara 0 hingga 1.

Hasil Rekomendasi:

Untuk contoh, user dengan ID 2 mendapat rekomendasi seperti:
- Aliens (1986)
- Total Recall (1990) 
- Terminator, The (1984)
- Fifth Element, The (1997)
- Twelve Monkeys (a.k.a. 12 Monkeys) (1995)

Model ini berhasil memberikan rekomendasi berdasarkan kesamaan film yang telah ditonton, sehingga bisa membantu pengguna menemukan film yang sesuai dengan selera mereka.

## Evaluation
Metrik evaluasi yang digunakan dalam proyek ini adalah Mean Squared Error (MSE). MSE mengukur selisih antara nilai yang diprediksi dan nilai sebenarnya, di mana semakin mendekati nilai 1 MSE, semakin baik kinerja model. Dalam proyek ini, nilai MSE yang dihasilkan oleh model adalah 0.87.

- Apakah sudah menjawab problem statment?
Sudah, model berhasil memberikan rekomendasi film yang sesuai dengan preferensi pengguna, sehingga memecahkan masalah utama.
- Apakah berhasil mencapai goals yang diharapkan?
Berhasil, model telah mencapai tujuan dengan meningkatkan kepuasan pengguna melalui rekomendasi film yang relevan berdasarkan rating.
- Apakah solusi statement yang kamu rencanakan berdampak?
berdampak, solusi ini membantu pengguna menemukan film lebih mudah, meningkatkan pengalaman dan keterlibatan pengguna dengan platform.
