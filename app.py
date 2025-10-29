import streamlit as st
from groq import Groq

# --------------------- PAGE CONFIG ---------------------
st.set_page_config(page_title="Lovers Lake 💞", page_icon="💌", layout="centered")

# --------------------- CUSTOM CSS ---------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ffdde1, #ee9ca7);
        }
        .main {
            background-color: rgba(255, 255, 255, 0.88);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #ff5e78;
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
        }
        .stButton > button {
            background-color: #ff85a1;
            color: white;
            border-radius: 20px;
            border: none;
            font-size: 16px;
            padding: 10px 25px;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #ff5e78;
            transform: scale(1.05);
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 15px;
            margin-bottom: 10px;
            display: inline-block;
            max-width: 80%;
        }
        .user-msg {
            background-color: #ffb6c1;
            color: #fff;
            align-self: flex-end;
            text-align: right;
        }
        .bot-msg {
            background-color: #fce4ec;
            color: #444;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------- API SETUP ---------------------
API_KEY = "YOUR_GROQ_API_KEY"  # 👈 apna Groq API key yahan daalo
client = Groq(api_key=API_KEY)

# --------------------- APP HEADER ---------------------
st.title("💞 Lovers Lake 💞")
st.caption("Where your heart talks and words bloom 🌸")

# --------------------- SESSION STATE (chat history) ---------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------- CHAT DISPLAY ---------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble user-msg'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-msg'>{msg['content']}</div>", unsafe_allow_html=True)

# --------------------- USER INPUT ---------------------
user_input = st.text_input("💌 Type your message here...", key="input")

# --------------------- SEND BUTTON ---------------------
if st.button("💖 Send"):
    if user_input.strip() != "":
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Send request to Groq model
        try:
            response = client.chat.completions.create(
                model="llama-3.1-70b-versatile",  # Recommended Groq model
                messages=[
                    {"role": "system", "content": "You are a romantic and caring AI called Lovers Lake."},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})

            # Rerun to show updated chat
            st.rerun()
        except Exception as e:
            st.error(f"💔 Error: {e}")

# --------------------- CLEAR CHAT BUTTON ---------------------
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.success("Chat cleared 💨")
