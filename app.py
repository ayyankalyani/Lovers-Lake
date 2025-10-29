import streamlit as st
from groq import Groq

st.title("💞 Lovers Lake - Ayyan ❤️ Laiba")

# Groq client initialization
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.write("Ask anything from Ayyan’s AI for Laiba 💌")

# User input
user_input = st.text_input("💬 Laiba, ask your question here:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message first!")
    else:
        with st.spinner("Ayyan’s AI is thinking... 💭"):
            try:
                response = client.chat.completions.create(
                    model="llama3-8b-8192",  # stable & supported model
                    messages=[
                        {"role": "system", "content": "You are Ayyan's AI version talking lovingly to Laiba. Respond sweetly, romantically, and kindly."},
                        {"role": "user", "content": user_input}
                    ],
                )
                reply = response.choices[0].message.content
                st.success("💖 Ayyan’s AI says:")
                st.write(reply)

            except Exception as e:
                st.error(f"Error: {e}")
