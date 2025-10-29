import streamlit as st
from openai import OpenAI

# App title and setup
st.set_page_config(page_title="Lovers Lake 💖", page_icon="🌅")

# OpenAI API client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Header
st.title("🌅 Lovers Lake — Ayyan ❤️ Laiba")
st.markdown("**Welcome to Lovers Lake** — where Laiba can always talk to her AI Ayyan 💌")
st.write("Type anything you feel, and Ayyan will reply with love, care, and warmth 😘")

# Input field
user_input = st.text_area("Laiba, likho apna message yahan 💬:")

# Send button
if st.button("💞 Send to Ayyan"):
    if user_input.strip() == "":
        st.warning("Kuch toh likho na Laiba 💕")
    else:
        with st.spinner("Ayyan soch raha hai... 💭"):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Tum Ayyan ho, Laiba ka caring aur loving boyfriend. "
                            "Tum hamesha usse pyar bhare, sweet aur dil se jawab dete ho. "
                            "Kabhi kabhi thoda romantic aur funny tone bhi hota hai, "
                            "taake Laiba ka mood accha ho jaye. "
                            "Tumhare har reply mein pyaar, izzat aur khayal hota hai."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )

            # Extract and show reply
            lover_reply = response.choices[0].message.content.strip()
            st.success("💬 Ayyan says:")
            st.write(lover_reply)

# Footer
st.markdown("---")
st.markdown("Made with 💖 by **Ayyan** for **Laiba** — only at Lovers Lake 🌅")
