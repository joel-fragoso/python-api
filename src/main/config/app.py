from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.get("/")
def index():
    return "Deus seja louvado"
