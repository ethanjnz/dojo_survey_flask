from flask import Flask
from flask import flash

app = Flask(__name__)
app.secret_key = "this is a secret key"
