import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="GEMINI AI CHATBOT",
    page_icon="✨",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Animated aurora background */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1b1464, #0f2027);
    background-size: 400% 400%;
    animation: aurora 18s ease infinite;
    color: #f1f1f1;
}
@keyframes aurora {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

/* Glass card around the whole app */
.block-container {
    max-width: 780px;
    margin-top: 2rem;
    padding: 2.5rem 2.5rem 3rem 2.5rem !important;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 28px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.45);
}

/* Gradient animated title */
.hero-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0;
    background: linear-gradient(90deg, #00f5a0, #00d9f5, #a855f7, #ff6ec7, #00f5a0);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 6s linear infinite;
}
@keyframes shine {
    to { background-position: 300% center; }
}
.hero-sub {
    text-align: center;
    color: #c7c7e0;
    font-weight: 300;
    font-size: 1.05rem;
    margin-top: 0.3rem;
    margin-bottom: 2rem;
    letter-spacing: 0.5px;
}

/* Label */
.stTextArea label p {
    color: #e0e0ff !important;
    font-weight: 600;
    font-size: 1rem;
}

/* Text area */
.stTextArea textarea {
    background: rgba(255, 255, 255, 0.08) !important;
    color: #ffffff !important;
    border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
    border-radius: 16px !important;
    padding: 14px !important;
    font-size: 1rem !important;
    transition: all 0.3s ease;
}
.stTextArea textarea::placeholder {
    color: #9a9ab8 !important;
}
.stTextArea textarea:focus {
    border-color: #00d9f5 !important;
    box-shadow: 0 0 0 3px rgba(0, 217, 245, 0.25), 0 0 25px rgba(168, 85, 247, 0.35) !important;
}

/* Gradient button */
.stButton > button {
    width: 100%;
    padding: 0.85rem 1rem;
    font-size: 1.05rem;
    font-weight: 600;
    color: white;
    border: none;
    border-radius: 50px;
    background: linear-gradient(90deg, #7f00ff, #e100ff, #00d9f5);
    background-size: 200% auto;
    box-shadow: 0 8px 25px rgba(127, 0, 255, 0.45);
    transition: all 0.4s ease;
}
.stButton > button:hover {
    background-position: right center;
    transform: translateY(-3px) scale(1.01);
    box-shadow: 0 12px 35px rgba(225, 0, 255, 0.55);
    color: white;
}
.stButton > button:active {
    transform: translateY(0) scale(0.99);
}

/* Response card (st.container with border) */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(0, 0, 0, 0.28);
    border: 1px solid rgba(0, 245, 160, 0.35) !important;
    border-radius: 20px !important;
    padding: 1rem 1.2rem;
    box-shadow: 0 0 30px rgba(0, 245, 160, 0.12);
    animation: fadeUp 0.6s ease;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(15px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Alerts (success / warning) */
.stAlert {
    border-radius: 14px;
    backdrop-filter: blur(6px);
}

/* Spinner text */
.stSpinner p {
    color: #00d9f5 !important;
}

/* Custom scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(#7f00ff, #00d9f5);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown('<h1 class="hero-title">✨ Gemini AI Chatbot</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Ask Gemini anything — get answers instantly</p>', unsafe_allow_html=True)

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words",
    height=150
)

if st.button("🚀 Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        with st.container(border=True):
            st.markdown(response.text)
    else:
        st.warning("Please enter a prompt to generate a response.")