import streamlit as st
import requests

st.set_page_config(page_title="Wellbeing Admin", layout="wide")
BASE_URL = "http://127.0.0.1:8000"

st.title("🛡️ Admin Wellbeing Dashboard")
st.subheader("Monitoring Data Real-time")

# Sidebar untuk statistik singkat
tasks = requests.get(f"{BASE_URL}/tasks").json()
st.sidebar.metric("Total Tugas", len(tasks))

# Main Content
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Daftar Fokus Hari Ini")
    if tasks:
        for i, t in enumerate(tasks):
            c1, c2 = st.columns([4, 1])
            c1.info(t)
            if c2.button("Hapus", key=f"del_{i}"):
                requests.delete(f"{BASE_URL}/tasks/{i}")
                st.rerun()
    else:
        st.write("Belum ada data masuk dari aplikasi mobile.")

with col2:
    st.write("### Kontrol LLM")
    st.button("Retrain Model")
    st.button("Export Dataset (JSON)")