from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

