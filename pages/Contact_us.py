import streamlit as st

from send_email import send_email

st.header('Contact us !')

with st.form("contact_form", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Send")
    if button:
        # print(f"Email: {user_email} \nMessage: {message}")
        send_email(user_email, message)
        st.info('Your email is sent successfully !')
