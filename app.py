# pip install streamlit openai

# streamlit 으로 파이썬으로 html,css 같은 기능을 쉽게 할 수 있음


import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")  # 터미널에서 streamlit run app.py # Always rerun

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [
        {
            "role": "system",
            "content": "Imagine the detail appeareance of the input. Response it shortly. it shortly around 20 words",
        }
    ]

    gpt_prompt.append({"role": "user", "content": user_input})

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.ChatCompletion.create(model="gpt-4", messages=gpt_prompt)

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALLE..."):
        dalle_response = openai.Image.create(prompt=prompt, size=size)

    st.image(dalle_response["data"][0]["url"])
