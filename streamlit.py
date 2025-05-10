import streamlit as st
from backend import get_data, query_agent

st.title("PDF Query Bot")
st.divider()
st.text("Upload a PDF and ask a question related to the PDF. Click on \"Generate\" to get the answer")

path, query = "", ""
slider = 0

with st.form("input"):
    path = st.text_input("File Path")
    query = st.text_area("Query")
    slider = st.select_slider("Points", options=list(range(1, 100)))
    submit = st.form_submit_button("Generate")


st.subheader("Output")
st.divider()

db = get_data(path)
answer = query_agent(query, slider, db)
if answer is not None:
    print(answer)
    st.write(answer)