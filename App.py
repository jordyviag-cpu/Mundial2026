import streamlit as st

st.title("Pronósticos Mundial FIFA 2026")

nombre = st.text_input("Nombre")

partido = st.selectbox(
    "Partido",
    [
        "México vs Sudáfrica",
        "Corea del Sur vs República Checa"
    ]
)

score = st.text_input("Score")

fecha = "11/06/2026"

st.write("Fecha:", fecha)

if st.button("Grabar"):
    st.success("Pronóstico registrado")
