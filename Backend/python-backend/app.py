# app.py
from flask import Flask
from flask_cors import CORS
from routes import main

app = Flask(__name__)
app.config.from_object('config.Config')
CORS(app)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
