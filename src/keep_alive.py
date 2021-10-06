from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

#função que podemos chamar para preparar nosso servidor e permitir que ele seja executado por ping.

def keep_alive():
    server = Thread(target=run)
    server.start()