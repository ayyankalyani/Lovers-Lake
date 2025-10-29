import streamlit as st
from groq import Groq

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="💞 Lovers Lake",
    page_icon="💌",
    layout="centered"
)

# ========== YOUR API KEY ==========
API_KEY = "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"  # 👈 Replace with your actual Groq API key (e.g. gsk_xxxxx)

client = Groq(api_key=API_KEY)

# ========== CUSTOM PAGE STYLING ==========
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f9c5d1 0%, #9795ef 100%);
            font-family: 'Poppins', sans-serif;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #ff8fab;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 25px;
            font-size: 16px;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff648c;
            transform: scale(1.05);
        }
        .chat-bubble {
            background-color: #ffe6eb;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
        }
        .bot-bubble {
            background-color: #e0e7ff;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# ========== APP TITLE ==========
st.title("💞 Lovers Lake")
st.write("Welcome to *Lovers Lake*, where Ayyan and Laiba can talk anytime, anywhere 🌸")

# ========== SESSION STATE FOR CHAT HISTORY ==========
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ========== USER INPUT ==========
user_input = st.text_input("💌 Laiba, ask anything from Ayyan's AI:")

# ========== SEND BUTTON ==========
if st.button("💖 Send Message"):
    if user_input.strip() != "":
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        try:
            # ✅ UPDATED MODEL (works in 2025)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # ✅ New Supported Groq Model
                messages=[
                    {"role": "system", "content": "You are Ayyan's romantic AI made for Laiba. Speak sweetly, lovingly, and always positive."},
                    *st.session_state.chat_history
                ]
            )

            bot_reply = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")

# ========== DISPLAY CHAT HISTORY ==========
st.markdown("### 💬 Chat History")
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"<div class='chat-bubble'><b>Laiba:</b> {chat['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><b>Ayyan's AI:</b> {chat['content']}</div>", unsafe_allow_html=True)
