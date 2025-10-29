import streamlit as st
from openai import OpenAI

# Connect to OpenAI API
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page setup
st.set_page_config(page_title="Lovers Lake 💖", page_icon="🌅")

# App Header
st.title("🌅 Lovers Lake — Ayyan ❤️ Laiba")
st.markdown("**Welcome to Lovers Lake** — where Laiba can always talk to her AI Ayyan 💌")

# Input section
user_input = st.text_area("Laiba, likho apna message yahan 💬:")

# On send
if st.button("💞 Send to Ayyan"):
    if user_input.strip() == "":
        st.warning("Kuch toh likho na Laiba 💕")
    else:
        with st.spinner("Ayyan soch raha hai... 💭"):
            # Generate romantic reply
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Tum Ayyan ho, Laiba ka caring aur loving boyfriend. "
                            "Tum hamesha usse pyaar bhare, gentle, aur sweet andaaz mein baat karte ho. "
                            "Tumhara tone hamesha affectionate, warm aur emotional hota hai. "
                            "Kabhi kabhi thoda funny bhi ho jaate ho, taake Laiba hase. "
                            "Hamesha Laiba ka respect aur khayal rakhte ho."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )

            lover_reply = response.choices[0].message.content.strip()

            # Display reply
            st.success("💬 Ayyan says:")
            st.write(lover_reply)

# Footer
st.markdown("---")
st.markdown("Made with 💖 by **Ayyan** for **Laiba** — at Lovers Lake 🌅")
