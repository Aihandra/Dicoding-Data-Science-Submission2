import streamlit as st
import numpy as np
import pickle

# Load model XGBoost (hasil training dari data yang sudah discaled)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Mapping pilihan input
APPLICATION_MODE_MAP = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    10: 'Ordinance No. 854-B/99',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
}

MOTHERS_OCCUPATION_MAP = {
    1: 'Secondary Education',
    2: 'Bachelor\'s Degree',
    3: 'Master\'s Degree',
    5: 'Doctorate',
    34: 'Unknown'
}

MOTHERS_QUALIFICATION_MAP = {
    0: 'Student',
    1: 'Legislative/Executive Bodies',
    2: 'Scientists',
    3: 'Technicians',
    4: 'Admin Staff',
    9: 'Unskilled Workers',
    90: 'Other',
    99: '(blank)'
}

COURSE_MAP = {
    33: 'Informatics',
    171: 'Nursing',
    8014: 'Tourism',
    9003: 'Management',
    9119: 'Marketing'
}

FATHERS_QUALIFICATION_MAP = {
    1: 'Primary Education',
    2: 'Secondary Education',
    3: 'Bachelor',
    4: 'Master',
    5: 'Doctorate',
    9: 'Unknown'
}

# Title
st.title("Prediksi Status Mahasiswa")

# Input
st.subheader("Silakan lengkapi data mahasiswa:")

col1, col2 = st.columns(2)

with col1:
    application_mode = st.selectbox("Metode Pendaftaran", list(APPLICATION_MODE_MAP.keys()), format_func=lambda x: APPLICATION_MODE_MAP[x])
    admission_grade = st.number_input("Nilai Penerimaan (0–200)", 0.0, 200.0, 120.0)
    previous_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 120.0)
    tuition_fees_up_to_date = st.radio("Pembayaran Lunas?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    debtor = st.radio("Memiliki Utang?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    scholarship_holder = st.radio("Penerima Beasiswa?", [1, 0], format_func=lambda x: "Ya" if x else "Tidak")
    gender = st.radio("Jenis Kelamin", [1, 0], format_func=lambda x: "Laki-laki" if x else "Perempuan")
    age_at_enrollment = st.number_input("Usia Saat Mendaftar", 15, 70, 18)
    curricular_units_1st_sem_approved = st.number_input("Unit Disetujui Semester 1", 0, 20, 5)
    curricular_units_1st_sem_grade = st.number_input("Nilai Rata-rata Semester 1", 0.0, 20.0, 10.0)

with col2:
    curricular_units_1st_sem_evaluations = st.number_input("Evaluasi Semester 1", 0, 50, 3)
    curricular_units_2nd_sem_approved = st.number_input("Unit Disetujui Semester 2", 0, 20, 5)
    curricular_units_2nd_sem_grade = st.number_input("Nilai Rata-rata Semester 2", 0.0, 20.0, 10.0)
    curricular_units_2nd_sem_evaluations = st.number_input("Evaluasi Semester 2", 0, 50, 3)
    curricular_units_2nd_sem_enrolled = st.number_input("Unit Diambil Semester 2", 0, 20, 6)
    mothers_occupation = st.selectbox("Pendidikan Ibu", list(MOTHERS_OCCUPATION_MAP.keys()), format_func=lambda x: MOTHERS_OCCUPATION_MAP[x])
    mothers_qualification = st.selectbox("Pekerjaan Ibu", list(MOTHERS_QUALIFICATION_MAP.keys()), format_func=lambda x: MOTHERS_QUALIFICATION_MAP[x])
    course = st.selectbox("Program Studi", list(COURSE_MAP.keys()), format_func=lambda x: COURSE_MAP[x])
    fathers_qualification = st.selectbox("Pendidikan Ayah", list(FATHERS_QUALIFICATION_MAP.keys()), format_func=lambda x: FATHERS_QUALIFICATION_MAP[x])
    curricular_units_1st_sem_enrolled = st.number_input("Unit Diambil Semester 1", 0, 20, 6)

# Prediksi
if st.button("Prediksi Status Mahasiswa"):
    input_data = np.array([[application_mode,
                            admission_grade,
                            previous_qualification_grade,
                            tuition_fees_up_to_date,
                            debtor,
                            scholarship_holder,
                            gender,
                            age_at_enrollment,
                            curricular_units_1st_sem_approved,
                            curricular_units_1st_sem_grade,
                            curricular_units_1st_sem_evaluations,
                            curricular_units_2nd_sem_approved,
                            curricular_units_2nd_sem_grade,
                            curricular_units_2nd_sem_evaluations,
                            curricular_units_2nd_sem_enrolled,
                            mothers_occupation,
                            mothers_qualification,
                            course,
                            fathers_qualification,
                            curricular_units_1st_sem_enrolled
                            ]])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    status_map = {0: 'Dropout', 1: 'Graduate', 2: 'Enrolled'}
    st.success(f"Status Mahasiswa: {status_map[prediction]}")
    st.write("Probabilitas:")
    for i, prob in enumerate(proba):
        st.write(f"{status_map[i]}: {prob*100:.2f}%")
