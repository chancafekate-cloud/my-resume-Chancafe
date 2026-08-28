import streamlit as st
from PIL import Image
import os

# Configuración de página
st.set_page_config(
    page_title="Liz Chancafe | Professional Resume",
    page_icon="👩‍💼",
    layout="wide"
)

# Estilos personalizados
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA: FOTO Y DATOS PERSONALES ---
col_photo, col_header = st.columns([1, 2.5], gap="medium")

with col_photo:
    if os.path.exists("image1.jpg"):
        image = Image.open("image1.jpg")
        st.image(image, use_container_width=True)
    else:
        st.info("📷 Upload 'image1.jpg' to view image")

with col_header:
    st.title("Liz Kateryn Chancafe Pisfil")
    st.subheader("Industrial Engineer | OSH & EHS Specialist | Data & AI Enthusiast")
    st.write("CIP License N° 260495")
    
    st.write("""
    📍 **Location:** Lima, Peru | 📞 **Phone:** +51 982 478 972  
    ✉️ **Email:** chancafekate@gmail.com  
    🔗 **LinkedIn:** [LinkedIn Profile](https://linkedin.com) | 🐙 **GitHub:** [github.com/chancafekate-cloud](https://github.com/chancafekate-cloud)
    """)

st.markdown("---")

# --- RESUMEN PROFESIONAL ---
st.header("📌 Professional Profile")
st.write("""
Licensed Industrial Engineer (CIP N° 260495) with **6 years of experience** in inspection, auditing, and management of 
Occupational Safety and Health (OSH/SST) and Environmental systems across the healthcare, construction, industrial, and 
agro-industrial sectors. Skilled in environmental risk management, metrics tracking, and integrating **Data Science and Artificial Intelligence tools** into corporate safety operations.
""")

# --- LOGOS Y HABILIDADES TÉCNICAS ---
st.header("🛠️ Technical Skills & Competencies")
st.markdown("""
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](#)
[![Microsoft Excel](https://img.shields.io/badge/Excel_Advanced-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](#)
[![ISO 45001](https://img.shields.io/badge/ISO_45001-003366?style=for-the-badge)](#)
[![ISO 14001](https://img.shields.io/badge/ISO_14001-006633?style=for-the-badge)](#)
[![ISO 9001](https://img.shields.io/badge/ISO_9001-990000?style=for-the-badge)](#)
""")

st.write("**Core Tools:** Microsoft Excel (Advanced), Word (Advanced), Power BI (Advanced), SAP (Basic), AutoCAD, Data Processing, SQL, Python, AI Tools.")

st.markdown("---")

# --- EXPERIENCIA PROFESIONAL ---
st.header("💼 Professional Experience")

with st.expander("🏛️ **INACAL (National Institute of Quality)** | OSH Specialist *(Aug 2025 – Jul 2026)*", expanded=True):
    st.write("""
    - **Performance Metrics:** Implemented Key Performance Indicators (KPIs) providing historical OSH traceability, improving preventive and corrective targeting by **50%**.
    - **Exposure Control:** Identified chemical and biological hazards, executing control measures such as mechanical ventilation enhancements and specialized PPE deployment.
    """)

with st.expander("🏥 **EsSalud / Alberto Sabogal Sologuren Hospital** | OSH Engineer *(Apr 2022 – Feb 2025)*"):
    st.write("""
    - **Risk Reduction:** Reduced locational and sharp-object accidents by **30%** (2024–2025) through targeted preventive protocols and technical auditing.
    - **Environmental Improvements:** Improved ventilation parameters in **10%** of hospital areas compared to the previous year.
    - **Scale Management:** Managed IPERC risk matrices and Risk Maps for over **3,000 personnel**, leading inspections, occupational monitoring, and accident investigations across support hospital networks in Lima Norte and Callao.
    - **Compliance:** Deployed COVID-19 safety checklists and regulatory health measures.
    """)

with st.expander("🛡️ **Alianza de Profesionales en Prevención de Riesgos S.A.C.** | Internal Auditor *(Jan 2022 – Jul 2025)*"):
    st.write("""
    - **Field Audits:** Executed **752 hours** of field audit work in OSH and Environmental systems under Law 29783, ISO 45001, ISO 9001, and ISO 14001 standards.
    """)

st.markdown("---")

# --- EDUCACIÓN Y CERTIFICACIONES ---
col_edu, col_cert = st.columns([1, 1], gap="large")

with col_edu:
    st.header("🎓 Education")
    st.write("""
    - **Master's Degree (Graduate Student) in Environmental & Corporate Safety Risk Management**  
      *Universidad Nacional de Trujillo* | Apr 2024
    - **Bachelor's Degree in Industrial Engineering**  
      *Universidad Católica Santo Toribio de Mogrovejo (USAT)* | Sep 2019
    """)
    
    st.header("🌐 Languages")
    st.write("""
    - **Spanish:** Native  
    - **English:** Intermediate
    """)

with col_cert:
    st.header("📜 Training & Certifications")
    st.write("""
    - **Data Processing (976 hrs):** ISIL, 2026.
    - **ISO 45001:2018 OSH Management Systems (16 hrs):** UNI, 2025.
    - **High-Risk Work Supervision (120 hrs):** ENCAP, 2024.
    - **Diploma in OSH & Environmental Inspection (256 hrs):** SUNAFIL / OEFA / UNMSM, 2022.
    - **Occupational Risk Prevention (16 hrs):** Ministry of Labor (MTPE).
    - **Fleet Management & Road Safety:** SUTRAN.
    - **Site Supervision & Construction Safety (32 hrs):** ENAPEP.
    - **Construction Safety & Health Management (48 hrs):** CIETSI.
    - **Professional Excel:** CEADEM.
    - **Speaker:** IV Academic Seminar in Engineering for Sustainable Development (USAT).
    """)
