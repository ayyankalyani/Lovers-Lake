import streamlit as st
from groq import Groq

# Streamlit setup
st.set_page_config(page_title="Lovers Lake 💖", page_icon="🌅")

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Header
st.title("🌅 Lovers Lake — Ayyan ❤️ Laiba")
st.markdown("**Welcome to Lovers Lake** — where Laiba can always talk to her AI Ayyan 💌")
st.write("Type anything you feel, and Ayyan will reply with love, care, and warmth 😘")

# User input
user_input = st.text_area("Laiba, likho apna message yahan 💬:")

# Button
if st.button("💞 Send to Ayyan"):
    if user_input.strip() == "":
        st.warning("Kuch toh likho na Laiba 💕")
    else:
        with st.spinner("Ayyan soch raha hai... 💭"):
            response = client.chat.completions.create(
                model="llama3-70b-8192",  # Groq ka best model
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Tum Ayyan ho, Laiba ka caring aur loving boyfriend. "
                            "Tum usse pyaar bhare, sweet aur dil se jawab dete ho. "
                            "Tumhara tone romantic, emotional, aur caring hota hai. "
                            "Laiba tumhare liye duniya jaisi important hai ❤️"
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )

            lover_reply = response.choices[0].message.content.strip()
            st.success("💬 Ayyan says:")
            st.write(lover_reply)

st.markdown("---")
st.markdown("Made with 💖 by **Ayyan** for **Laiba** — only at Lovers Lake 🌅")
