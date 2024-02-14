from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config) #adding configuraion file

from app import routes