#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://waled:root@localhost/data"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug==True, host='0.0.0.0')
