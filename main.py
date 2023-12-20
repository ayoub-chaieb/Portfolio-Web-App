import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ayoub CHAIEB")
    content = """
        Results-driven enthusiast with a strong passion for technology, particularly in the realm of AI and high-tech innovation. Aspiring IT
        professional with a desire to contribute to cutting-edge projects. Proficient in 3D modeling, which reflects my creativity. Committed to gaining hands-on experience in IT.
    """
    st.info(content)

content2 = """You will find below some of my achievements, feel free to contact me"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for i, row in df[::2].iterrows():
        st.header(row["title"])
        st.image("images/" + row['image'])
        st.write(row["description"])
        st.link_button("Go to gallery", row['url'])
        # st.write(f"[Go to gallery]({row['url']})")

with col4:
    for i, row in df[1::2].iterrows():
        st.header(row["title"])
        st.image("images/" + row['image'])
        st.write(row["description"])
        st.link_button("Go to gallery", row['url'])
        # st.write(f"[Go to gallery]({row['url']})")
