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

import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
