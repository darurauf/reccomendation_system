# -*- coding: utf-8 -*-
"""Reccomendation_Dicoding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VtszhFFzln7Pscxt5y8HMbkXOwJljVpR

# **Import Library**

Kita akan menggunakan library pandas untuk akses dan mengatur data serta sklearn untuk menggunakan metode cosine similiarity
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

"""# **Load Dataset**

Dataset yang akan digunakan adalah dataset dari Movielens serta rating untuk film tersebut. Kita akan menggunakan 20000 data saja agar mempermudah komputasi
"""

from google.colab import drive
drive.mount('/content/drive')

movies_path = '/content/drive/MyDrive/movie.csv'
rating_path = '/content/drive/MyDrive/rating.csv'
movies = pd.read_csv(movies_path).head(20000)
rating = pd.read_csv(rating_path).head(20000)

print("Dataset Movies: ")
print(movies.head())
print("\nDataset Rating: ")
print(rating.head())

"""# **Data Preparation**

Dikarenakan kita menggunakan collaborative filtering dan memiliki 2 dataset yang berhubungan. Kita perlu untuk menggabungkan kedua dataset tersebut dengan patokan userId, juga akan melakukan data preprocessing seperti mengatasi missing values dan mengubah data menjadi pivot table agar data lebih terorganisir
"""

# Gabungkan kedua dataset
data = pd.merge(rating, movies, on='movieId')

# Membuat Pivot table
data_pivot = data.pivot_table(index='userId', columns='title', values='rating')

# Mengatasi missing values
data_pivot.fillna(0, inplace=True)

print("Dataset setelah melakukan merge : ")
print(data.head())
print("\nDataset setelah melakukan pivot : ")
print(data_pivot.head())

"""# **Mencari Kesamaan Antar User**

Kali ini kita akan menggunakan metode cosine similarity untuk kemiripan rating film antar para user
"""

data_similarity = cosine_similarity(data_pivot.T)

# Membuat dataframe setelah melakukan cosine similarity
data_similarity_df = pd.DataFrame(data_similarity, index=data_pivot.columns, columns=data_pivot.columns)

print(data_similarity_df.head())

"""# **Mencoba Sistem Rekomendasi**

Mencoba tes fungsi rekomendasi dan evaluasi menggunakan MSE
"""

# Fungsi untuk memberikan rekomendasi
def recommend_movies(user_id, data_pivot, data_similarity_df, num_recommendations=5):
    # Mendapatkan film yang sudah ditonton oleh pengguna
    user_ratings = data_pivot.loc[user_id]
    watched_movies = user_ratings[user_ratings > 0].index.tolist()

    # Membuat dictionary untuk menyimpan skor rekomendasi
    recommendations = {}

    # Menghitung skor rekomendasi untuk setiap film yang belum ditonton
    for movie in data_pivot.columns:
        if movie not in watched_movies:
            sim_scores = data_similarity_df[movie]
            score = sum(sim_scores[movie_watched] * user_ratings[movie_watched] for movie_watched in watched_movies)
            recommendations[movie] = score

    # Mengurutkan rekomendasi berdasarkan skor
    recommended_movies = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]

    return [movie[0] for movie in recommended_movies]

# Fungsi untuk evaluasi
def evaluate_model(data_pivot, data_similarity_df):
    mse_list = []

    for user_id in data_pivot.index:
        user_ratings = data_pivot.loc[user_id]
        watched_movies = user_ratings[user_ratings > 0].index.tolist()

        for movie in watched_movies:
            # Menghitung estimasi rating
            sim_scores = data_similarity_df[movie]
            estimated_rating = sum(sim_scores[movie_watched] * user_ratings[movie_watched] for movie_watched in watched_movies) / sum(sim_scores[movie_watched] for movie_watched in watched_movies)
            actual_rating = user_ratings[movie]

            # Menghitung MSE
            mse_list.append((actual_rating, estimated_rating))  # Simpan tuple (actual_rating, estimated_rating)

    # Menghitung MSE
    actual_ratings, estimated_ratings = zip(*mse_list)  # Pisahkan actual dan estimated
    return mean_squared_error(actual_ratings, estimated_ratings)

# Contoh penggunaan
user_id = 2  # Ganti dengan userId yang diinginkan
recommended_movies = recommend_movies(user_id, data_pivot, data_similarity_df)
print(f"Rekomendasi film untuk pengguna {user_id}: {recommended_movies}")

# Evaluasi model
mse = evaluate_model(data_pivot, data_similarity_df)
print(f"MSE dari model: {mse}")