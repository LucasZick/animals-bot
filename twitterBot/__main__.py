from multiprocessing import Process
from flask import Flask

from twitterBot.config import CONFIG
import twitterBot.bot as Bot

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "I'm still alive!"

def start():
    Process(target=Bot.run).start()
    app.run(host="0.0.0.0", port=int(CONFIG.PORT))

start()
