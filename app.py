from flask import Flask, redirect, request
import os

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

@app.route("/")
def index():
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"response_type=code&"
        f"scope=https://www.googleapis.com/auth/contacts.readonly&"
        f"access_type=offline"
    )
    return f'<a href="{auth_url}">Login with Google</a>'

@app.route("/oauth2callback")
def callback():
    code = request.args.get("code")
    return f"Authorization Code: {code}"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
