import streamlit as st
from modules.phishing_detector import load_model as load_phishing_model, predict_url
from modules.ids_detector import predict_intrusion, predict_intrusion_from_csv
from modules.malware_detector import predict_file_features as predict_malware
from modules.ransomware_detector import predict_ransomware
from modules.brute_force_detector import predict_brute_force, predict_brute_force_from_csv

# Load models once
phishing_model = load_phishing_model()

# Sidebar navigation
st.set_page_config(page_title="AI CyberSecure App", layout="wide")
st.sidebar.title("🛡️ AI CyberSecure App")
module = st.sidebar.radio("Select Module", [
    "Home",
    "Phishing URL Detection",
    "Intrusion Detection (NSL-KDD)",
    "Malware Detection",
    "Ransomware Behavior Detection",
    "Brute Force Attack Detection"
])

# Style for consistent design
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# --- HOME ---
if module == "Home":
    st.title("🛡️ AI CyberSecure App")
    st.markdown("""
Welcome to the AI CyberSecure App. This app provides intelligent detection for various cybersecurity threats:

- 🔗 **Phishing URL Detection**
- 📡 **Intrusion Detection System (NSL-KDD)**
- 🦠 **Malware File Threats**
- 🧬 **Ransomware Behavior Detection**
- 🔓 **Brute Force Attack Detection**

Select a module from the sidebar to get started.
    """)

# --- PHISHING MODULE ---
elif module == "Phishing URL Detection":
    st.title("Phishing URL Detection")
    st.markdown("<hr style='border:2px solid #e74c3c'>", unsafe_allow_html=True)
    phishing_url = st.text_input("Paste a suspicious URL to check if it's phishing")

    if st.button("Scan URL"):
        if phishing_url:
            result = predict_url(phishing_url.strip(), phishing_model)
            st.success(f"Result: **{result}**")
        else:
            st.warning("Please enter a valid URL.")

# --- IDS MODULE ---
elif module == "Intrusion Detection (NSL-KDD)":
    st.title("Intrusion Detection System (NSL-KDD)")
    st.markdown("<hr style='border:2px solid #3498db'>", unsafe_allow_html=True)
    tabs = st.tabs(["Manual Entry", "CSV Upload"])

    with tabs[0]:
        st.subheader("Manual Input")
        st.markdown("Paste 41 comma-separated numerical features:")
        features_input = st.text_area("Enter 41 comma-separated features", height=100)
        if st.button("Detect Intrusion"):
            try:
                features = [float(i.strip()) for i in features_input.split(",")]
                result = predict_intrusion(features)
                st.success(f"IDS Result: {result}")
            except:
                st.error("Invalid input. Ensure 41 comma-separated numerical values.")

    with tabs[1]:
        st.subheader("CSV Upload")
        uploaded_file = st.file_uploader("Upload a CSV file (41 features per row)", type=["csv"])
        if uploaded_file:
            result_df, error = predict_intrusion_from_csv(uploaded_file)
            if error:
                st.error(error)
            else:
                st.dataframe(result_df)

# --- MALWARE MODULE ---
elif module == "Malware Detection":
    st.title("Malware Detection (Static Features)")
    st.markdown("<hr style='border:2px solid #e67e22'>", unsafe_allow_html=True)
    malware_input = st.text_area("Enter 41 comma-separated static features extracted from a file")
    if st.button("Scan File"):
        try:
            features = [float(i.strip()) for i in malware_input.split(",")]
            result = predict_malware(features)
            st.success(f"Malware Scan Result: {result}")
        except:
            st.error("Please enter exactly 41 numerical values.")

# --- RANSOMWARE MODULE ---
elif module == "Ransomware Behavior Detection":
    st.title("Ransomware Behavior Detection")
    st.markdown("<hr style='border:2px solid #9b59b6'>", unsafe_allow_html=True)
    ransom_input = st.text_area("Enter 30 comma-separated behavioral/static features")
    if st.button("Detect Ransomware"):
        try:
            features = [float(i.strip()) for i in ransom_input.split(",")]
            result = predict_ransomware(features)
            st.success(f"Ransomware Detection Result: {result}")
        except:
            st.error("Please enter exactly 30 numerical values.")

# --- BRUTE FORCE MODULE ---
elif module == "Brute Force Attack Detection":
    st.title("Brute Force Attack Detection")
    st.markdown("<hr style='border:2px solid #34495e'>", unsafe_allow_html=True)
    tabs = st.tabs(["Manual Entry", "CSV Upload"])

    with tabs[0]:
        st.subheader("Manual Input")
        bf_input = st.text_input("Enter 3 comma-separated features: password_attempts, login_success, timestamp_hour")
        if st.button("Detect Brute Force"):
            try:
                features = [float(x.strip()) for x in bf_input.split(",")]
                result = predict_brute_force(features)
                st.success(f"Brute Force Detection Result: {result}")
            except:
                st.error("Please provide 3 valid numbers.")

    with tabs[1]:
        st.subheader("CSV Upload")
        uploaded_file = st.file_uploader("Upload brute_force_logs.csv", type=["csv"])
        if uploaded_file:
            df, error = predict_brute_force_from_csv(uploaded_file)
            if error:
                st.error(error)
            else:
                st.dataframe(df)
