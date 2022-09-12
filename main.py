from flask import Flask, get_json, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.hostnet.nl'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aspnetcore@noonecio.us'
app.config['MAIL_PASSWORD'] = 'Aschap32!Aschap32!'
mail = Mail(app)

@app.post('/contact')
def contact():
    json = get_json()
    msg = Message('Customer', sender="aspnetcore@noonecio.us", recipients=["noonecio.us@outlook.com"])
    msg.body = json['body']
    mail.send(msg)
    return 200, 