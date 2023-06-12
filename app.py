import streamlit as st
import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt

def main():
    st.title("Aplikasi Uji Hipotesis Dua Populasi Varians")
    
    # Memasukkan data dari pengguna
    st.subheader("Masukkan Data Populasi Pertama:")
    data_pop1 = st.text_area("Masukkan data populasi pertama, dipisahkan dengan koma (misal: 1,2,3,4)")
    
    st.subheader("Masukkan Data Populasi Kedua:")
    data_pop2 = st.text_area("Masukkan data populasi kedua, dipisahkan dengan koma (misal: 1,2,3,4)")
    
    # Mengonversi data menjadi array numpy
    try:
        pop1 = np.array([float(x.strip()) for x in data_pop1.split(",")])
        pop2 = np.array([float(x.strip()) for x in data_pop2.split(",")])
    except:
        st.error("Terjadi kesalahan dalam memproses data. Pastikan format input benar.")
        return
    
    # Menampilkan data
    st.subheader("Data Populasi Pertama:")
    st.write(pop1)
    
    st.subheader("Data Populasi Kedua:")
    st.write(pop2)
    
    # Menghitung varians
    var1 = np.var(pop1, ddof=1)
    var2 = np.var(pop2, ddof=1)
    
    # Menampilkan varians
    st.subheader("Varians Populasi Pertama:")
    st.write(var1)
    
    st.subheader("Varians Populasi Kedua:")
    st.write(var2)
    
    # Menghitung statistik uji
    n1 = len(pop1)
    n2 = len(pop2)
    statistic = var1 / var2
    
    # Menghitung derajat kebebasan
    df1 = int(n1 - 1)
    df2 = int(n2 - 1)
    
    # Menghitung p-value
    p_value = 2 * min(1 - f.cdf(statistic, df1, df2), f.cdf(statistic, df1, df2))

    
    # Menampilkan hasil uji hipotesis
    st.subheader("Hasil Uji Hipotesis:")
    st.write("Statistik Uji:", statistic)
    st.write("Derajat Kebebasan 1:", df1)
    st.write("Derajat Kebebasan 2:", df2)
    st.write("Nilai p-value:", p_value)
    
    # Membuat grafik tabel distribusi F dan grafik p-value
    x = np.linspace(0, max(statistic * 2, 10), 1000)
    y_f = f.pdf(x, df1, df2)
    y_pvalue = np.where(x >= statistic, y_f, 0)
    
    fig, ax = plt.subplots()
    ax.plot(x, y_f, 'r-', lw=2, label='Distribusi F')
    ax.fill_between(x, y_f, where=(x >= statistic), alpha=0.5, color='gray', label='p-value')
    ax.plot(x, y_pvalue, 'b-', lw=2, label='p-value (zoomed in)')
    ax.legend(loc='best')
    ax.set_xlabel('Statistik Uji')
    ax.set_ylabel('Densitas')
    ax.set_title('Tabel Distribusi F dan Grafik p-value')
    
    # Menampilkan grafik tabel distribusi F dan grafik p-value
    st.subheader("Grafik Tabel Distribusi F dan Grafik p-value")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
