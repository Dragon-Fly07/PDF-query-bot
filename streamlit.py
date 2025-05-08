import streamlit as st
from backend import get_data, query_agent

st.title("PDF Answer Generator")
st.divider()
st.text("Upload a PDF and ask a question related to the PDF. Click on \"Generate\" to get the answer")

path, query = "", ""
slider = 0

with st.form("input"):
    path = st.text_input("File Path")
    query = st.text_area("Query")
    slider = st.select_slider("Marks", options=[2, 4, 6, 8, 12])
    submit = st.form_submit_button("Generate")


db = get_data(path)
answer = query_agent(query, slider, db)
if answer is not None:
    st.markdown(answer)