from google import genai
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key = "AIzaSyBMuyM144kGFP4yJ9flotNtfEZYWN7NhAg")

st.title("AI Chat Application⚛️")
# # st.markdown("ai")

if "messages" not in st.session_state:
    st.session_state.messages = [{
         "role":"AI",
        "content":"Hello! How can i assist you today?"
    }
    ]

# messages = [
#     { "role":"AI",
#         "content":"Hello! How can i assist you today?"
#     },S
#     {
#         "role":"User",
#         "content":"can you tell me joke"
#     },
#     {
#         "role":"AI",
#         "content":"Sure! why did the scarecrow win an award? Beacause he was outstanding in his field!"
#     }
# ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Enter your message here.....")

if(user_input):
    st.session_state.messages.append({
        "role":"User",
        "content":user_input
    })


    with st.chat_message("User"):
        st.markdown(user_input)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = list(map(lambda message: message["role"]+": "+message["content"],st.session_state.messages))
        )
    st.session_state.messages.append({
        "role":"AI",
        "content":response.text
    })

    with st.chat_message("AI"):
        st.markdown(response.text)

    