import smtplib, ssl


def send_email(user_email: str, message: str):
    host = "smtp.gmail.com"
    port = 465
    password = "lfoihpbbwvozdwiw"
    receiver = "ayoubchaieb75@gmail.com"
    email = f"""\
Subject: {user_email} wanted to reach you! || Streamlit Portfolio App 

From: {user_email}
{message}
"""
    # consider showing the name of the sender (from email) by using som substring
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, email)
