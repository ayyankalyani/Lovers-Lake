import streamlit as st
from groq import Groq

st.set_page_config(page_title="Lovers Lake 💞", page_icon="💖")
st.title("💞 Lovers Lake - Ayyan ❤️ Laiba")
st.write("Laiba, you can talk to Ayyan’s AI anytime you miss him 💌")

# --- Initialize Groq client using secret key ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- User input box ---
user_input = st.text_input("💬 Laiba, ask something from Ayyan's AI:")

# --- When button is clicked ---
if st.button("Send Message 💌"):
    if user_input.strip() == "":
        st.warning("Please write something first, Laiba! 💕")
    else:
        with st.spinner("Ayyan’s AI is thinking... 💭"):
            try:
                # Use new supported model
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",  # ✅ Active model
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are Ayyan’s AI version, made lovingly for Laiba. "
                                "Talk like Ayyan would — kind, romantic, funny, and caring. "
                                "Always answer warmly and lovingly."
                            ),
                        },
                        {"role": "user", "content": user_input},
                    ],
                )

                reply = response.choices[0].message.content
                st.success("💖 Ayyan’s AI says:")
                st.write(reply)

            except Exception as e:
                st.error(f"Error: {e}")
