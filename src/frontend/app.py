import streamlit as st
import requests

st.title("Outing Recommender")

if st.button("Send"):

    response = requests.get(
        "http://127.0.0.1:8000/api/baseroute/"
    )

    st.write(response.json())


#    