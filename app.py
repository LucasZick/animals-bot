from multiprocessing import Process
from flask import Flask

from animals_bot.config import CONFIG
import animals_bot.bot as Bot

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "I'm still alive!"

def start():
    Process(target=Bot.run).start()
    if CONFIG.TEST != '':
        app.run(host="0.0.0.0", port=int(CONFIG.PORT))
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=int(CONFIG.PORT))

if  __name__ == "__main__":
    start()