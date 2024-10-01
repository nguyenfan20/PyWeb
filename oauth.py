# oauth.py
from authlib.integrations.flask_client import OAuth

def init_oauth(app):
    oauth = OAuth(app)
    facebook = oauth.register(
        name='facebook',
        client_id=app.config['FACEBOOK_CLIENT_ID'],
        client_secret=app.config['FACEBOOK_CLIENT_SECRET'],
        authorize_url='https://www.facebook.com/dialog/oauth',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        redirect_uri=app.config['FACEBOOK_REDIRECT_URI'],
        client_kwargs={'scope': 'email'}
    )
    return facebook
