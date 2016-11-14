from flask import Flask
import os
import word_frequency

app = Flask(__name__)


@app.route('/')
def hello_world():
    word = word_frequency.random_word()
    return word


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
