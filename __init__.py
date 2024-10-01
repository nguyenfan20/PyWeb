from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
from itsdangerous import URLSafeTimedSerializer
from oauthlib.oauth2 import WebApplicationClient
from flask_mail import Mail
from .config import Config
from .oauth import init_oauth
import os

# If your server is not parametrized to allow HTTPS,
# the fetch_token method will raise an "oauthlib.oauth2.rfc6749.errors.InsecureTransportError".
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/tmdt?charset=utf8mb4"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:tuan0512@localhost/tmdt?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "(A*FA(GAGASDA*&"

app.config["CLOUDINARY_INFO"] = {
"cloud_name" : "natscloud",
"api_key" : "669999992192735",
"api_secret": "7-zbW0Pat43_axsYVZ2ULRTe5zY"
}

# Configuration Login with google
GOOGLE_CLIENT_ID = "291311646452-lrkbrgq433p0c78ef8qq2cdj8ljaptt2.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
"https://accounts.google.com/.well-known/openid-configuration"
)

app.config.from_object(Config)

# Khởi tạo OAuth cho Facebook
facebook = init_oauth(app)

# Configure through environment variables:
app.config["PAYPAL-SANDBOX-CLIENT-ID"] = "Aa6Hn8C93yInGY6oa-St9YgzwOxToXoD_-iqvbmpcn8vl-0qVFqF0Qr6Z5F6DjWVSR4OMuaFNVg7ewEk"
app.config["PAYPAL-SANDBOX-CLIENT-SECRET"] = "EJSfWZBrSsHIkqFwB-jPlgpFQNlaw5BG2TQEarvw6cY9JSg4noNbyERKqvHy21Na-C33CuYX_J8J4Csj"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nguyenphan0705v@gmail.com'
app.config['MAIL_PASSWORD'] = '0908989739by'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ('Laptop UTE', 'nguyenphan0705v@gmail.com')

app.config["PAGE_SIZE"] = 9
db = SQLAlchemy(app=app)
my_login = LoginManager(app=app)
client = WebApplicationClient(GOOGLE_CLIENT_ID)  # OAuth 2 client setup
mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)

cloudinary.config(cloud_name = app.config["CLOUDINARY_INFO"]['cloud_name'],
api_key = app.config["CLOUDINARY_INFO"]['api_key'],
api_secret = app.config["CLOUDINARY_INFO"]['api_secret'])



CART_KEY = "cart"

# partner_code = "MOMOYTDW20211109"
# access_key = "kG8pmfc4K4M3bFqm"
# secret_key = "nI3noEFbEHynhTR683yqDEqf100Hp1Z0"
# api_endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"

momo = {
    "endpoint": "https://test-payment.momo.vn/gw_payment/transactionProcessor",
    "partnerCode": "MOMOORNE20211031",
    "accessKey": "ULvMSUhENodZ2stN",
    "secretKey": "i3tq9bB1lPHpIwsat6hPMgUoj5yCiLPv",
    "orderInfo": "pay with MoMo",
    "returnUrl": "http://127.0.0.1:5000/momo/payment-result",
    "notifyUrl": "http://127.0.0.1:5000/momo/payment-result",
    "amount": "",
    "orderId": "",
    "requestId": "",
    "requestType": "captureMoMoWallet",
    "extraData": ""
}
# tuan05122001@personal.example.com
# tuan@0512
# def create_app():
#     app = Flask(__name__)

#     app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:admin@localhost/tmdt?charset=utf8mb4"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.secret_key = "(A*FA(GAGASDA*&"

#     # Cấu hình Google OAuth
#     app.config["GOOGLE_CLIENT_ID"] = "919352421263-e18mqjhotmb6l176kflviroomrbbd5qd.apps.googleusercontent.com"
#     app.config["GOOGLE_CLIENT_SECRET"] = "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"

#     # Other configurations...
#     app.config["CLOUDINARY_INFO"] = {
#         "cloud_name": "natscloud",
#         "api_key": "669999992192735",
#         "api_secret": "7-zbW0Pat43_axsYVZ2ULRTe5zY"
#     }

#     # Setup OAuth and Mail configurations
#     app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#     app.config['MAIL_PORT'] = 587
#     app.config['MAIL_USERNAME'] = 'nguyenphan0705v@gmail.com'
#     app.config['MAIL_PASSWORD'] = '0908989739by'
#     app.config['MAIL_USE_TLS'] = True
#     app.config['MAIL_USE_SSL'] = False
#     app.config['MAIL_DEFAULT_SENDER'] = ('Laptop UTE', 'nguyenphan0705v@gmail.com')

#     # Initialize extensions
#     db.init_app(app)
#     my_login.init_app(app)
#     mail.init_app(app)
#     client = WebApplicationClient(app.config['GOOGLE_CLIENT_ID'])

#     # #Đăng ký blueprint
#     # from .index import index_bp
#     # app.register_blueprint(index_bp)

#     # Cloudinary config
#     cloudinary.config(
#         cloud_name=app.config["CLOUDINARY_INFO"]['cloud_name'],
#         api_key=app.config["CLOUDINARY_INFO"]['api_key'],
#         api_secret=app.config["CLOUDINARY_INFO"]['api_secret']
#     )

#     return app