import os
from multiprocessing import Process

from flask import Flask

import bot as Bot

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return "I'm still alive!"

def start():
    Process(target=Bot.run).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))

start()
