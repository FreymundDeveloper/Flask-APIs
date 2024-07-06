from flask import render_template, request, url_for
from flask_mail import Mail, Message

mail = Mail()

def send_email(user, email):
        link = request.url_root[:-1] + url_for('userconfirm', user_id=user)

        msg = Message(subject='Confirm Your Login', sender='emailflask@mail.com', recipients=[email])
        msg.html = render_template('user_confirm.html', link=link)
        mail.send(msg)