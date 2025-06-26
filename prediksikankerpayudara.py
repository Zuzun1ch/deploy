import streamlit as st
import numpy as np
import joblib

st.title("Prediksi Kanker Payudara (Jinak/Ganas)")

# Input form
with st.form("form_prediksi"):
    st.subheader("Masukkan nilai fitur:")
    
    Clump_thickness = st.slider("Clump Thickness", 1, 10, 5)
    Uniformity_of_cell_size = st.slider("Uniformity of Cell Size", 1, 10, 5)
    Uniformity_of_cell_shape = st.slider("Uniformity of Cell Shape", 1, 10, 5)
    Marginal_adhesion = st.slider("Marginal Adhesion", 1, 10, 5)
    Single_epithelial_cell_size = st.slider("Single Epithelial Cell Size", 1, 10, 5)
    Bare_nuclei = st.slider("Bare Nuclei", 1, 10, 5)
    Bland_chromatin = st.slider("Bland Chromatin", 1, 10, 5)
    Normal_nucleoli = st.slider("Normal Nucleoli", 1, 10, 5)
    Mitoses = st.slider("Mitoses", 1, 10, 1)
    
    submitted = st.form_submit_button("Prediksi")

# Jika tombol ditekan, lakukan prediksi
if submitted:
    # Siapkan input
    input_data = np.array([[ 
        Clump_thickness,
        Uniformity_of_cell_size,
        Uniformity_of_cell_shape,
        Marginal_adhesion,
        Single_epithelial_cell_size,
        Bare_nuclei,
        Bland_chromatin,
        Normal_nucleoli,
        Mitoses
    ]])

    # Muat model
    model = joblib.load("model_knn.pkl")  # Ganti dengan model Anda

    # Prediksi
    pred = model.predict(input_data)[0]

    # Konversi hasil ke label deskriptif
    if pred == 2 or pred == "2" or pred == "Jinak":
        label = "Kanker Payudara Jinak"
    elif pred == 4 or pred == "4" or pred == "Ganas":
        label = "Kanker Payudara Ganas"
    else:
        label = f"Tak dikenal ({pred})"

    # Tampilkan hasil
    st.success(f"Hasil Prediksi: **{label}**")
