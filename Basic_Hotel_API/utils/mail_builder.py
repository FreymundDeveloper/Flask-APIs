from flask import request, url_for
from flask_mail import Mail, Message

mail = Mail()

def send_email(user, email):
        link = request.url_root[:-1] + url_for('userconfirm', user_id=user)

        msg = Message(subject='Hello', sender='emailflask@mail.com', recipients=[email])
        msg.body = "Click here {} to confirm you activate.".format(link)
        mail.send(msg)