import streamlit as st
import os
import openai
import json

st.title("Faz Tudo Por ti Do André")




prompt = st.text_input("O que queres fazer:")


if st.button("Submeter"):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    st.write(response["choices"][0]["text"])

