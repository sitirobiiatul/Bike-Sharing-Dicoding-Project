# -*- coding: utf-8 -*-
"""Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MTVzGduFq41NpecAfS_EqmuSm6FJeUPP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    all_data = pd.read_csv("https://raw.githubusercontent.com/sitirobiiatul/Bike-Sharing-Dicoding-Project/main/Dashboard/all_data.csv")
    return all_data

all_data = load_data()

def create_avg_holiday_df(df):
  avg_holiday_df = all_data.groupby('holiday_daily')['cnt_daily'].mean().reset_index().sort_values("cnt_daily")
  return avg_holiday_df

def create_rental_jam_df(df):
  rental_jam_df = all_data.groupby('hr')['cnt_hourly'].mean()
  return rental_jam_df

# SIDEBAR
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Siti Robiiatul Adawiyyah**")
st.sidebar.markdown(
    "**• Dicoding: [sitirobiiatul](https://www.dicoding.com/users/sitirobiiatul)**")

# Set page title
st.title("Bike-Sharing Dashboard")

st.sidebar.title("Dataset Bike-Sharing")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Cleaned Data")
    st.write(all_data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(all_data.describe())

# Show dataset source
st.sidebar.markdown("[Download Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)")

# Pastikan kolom 'dteday' memiliki tipe data datetime
all_data['dteday'] = pd.to_datetime(all_data['dteday'])

min_date = all_data['dteday'].min()
max_date = all_data['dteday'].max()

# Kemudian, Anda dapat menggunakan variabel min_date sebagai min_value di st.date_input()
with st.sidebar:
  start_date, end_date = st.date_input(
      label='Date Filter',
      min_value=min_date,
      max_value=max_date,
      value=[min_date, max_date]
      )

main_df = all_data[(all_data['dteday'] >= str(start_date)) &
 (all_data['dteday'] <= str(end_date))]

avg_holiday_df = create_avg_holiday_df(main_df)

rental_jam_df = create_rental_jam_df(main_df)

# Container dengan bar plot
with st.container():
  st.subheader('Penyewa Sepeda berdasarkan Hari')
# Bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=all_data, x='weekday_daily', y='cnt_daily', color='#5F9EA0')
  ax.set(title='Total Penyewa Sepeda Berdasarkan Hari')
  plt.xlabel('Hari')
  plt.ylabel('Total Penyewa')

# Menampilkan plot di Streamlit
  st.pyplot(fig)

#Container dengan bar plot
with st.container():
  st.subheader('Penyewa Sepeda berdasarkan Jam')
# Bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=avg_holiday_df, x=rental_jam_df.index, y=rental_jam_df.values, color='#D8BFD8')
  ax.set(title='Pola Jumlah Sewa Sepeda Harian Berdasarkan Jam')
  plt.xlabel('Jam')
  plt.ylabel('Total Penyewa')

  # Menampilkan plot di Streamlit
  st.pyplot(fig)

with st.container():
  st.subheader('Penyewa Sepeda berdasarkan Bulan')
# Bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=all_data, x='mnth_daily', y='cnt_daily', hue='yr_daily', palette = 'Set2')
  ax.set(title='Total Penyewa Sepeda Berdasarkan Bulan')
  plt.xlabel('Bulan')
  plt.ylabel('Total Penyewa')

# Menampilkan plot di Streamlit
  st.pyplot(fig)

with st.container():
  st.subheader('Penyewa Sepeda berdasarkan Musim')
# Bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=all_data, x='season_daily', y='cnt_daily', hue='yr_daily', palette = 'Set2')
  ax.set(title='Total Penyewa Sepeda Berdasarkan Bulan')
  plt.xlabel('Musim')
  plt.ylabel('Total Penyewa')

# Menampilkan plot di Streamlit
  st.pyplot(fig)

with st.container():
  st.subheader('Perbedaan Penyewaan Sepeda di Hari Kerja (Workingday) dan Hari Libur (Holiday)')
# Bar plot
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(data=avg_holiday_df, x='holiday_daily', y='cnt_daily', palette='Set1')
  ax.set(title='Rata-rata Penyewaan Sepeda pada Hari Libur')
  plt.xlabel('Hari Libur')
  plt.ylabel('Total Penyewa')
  plt.xticks([0, 1], ['Tidak Libur', 'Libur'])

# Menampilkan plot di Streamlit
  st.pyplot(fig)

# Hide Streamlit Style
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
