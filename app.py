from flask import Flask
import word_frequency

app = Flask(__name__)


@app.route('/')
def hello_world():
    word = word_frequency.random_word()
    return word



if __name__ == '__main__':
    app.run()
