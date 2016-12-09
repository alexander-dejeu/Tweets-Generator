from flask import Flask, render_template
import os
import word_frequency

app = Flask(__name__)


@app.route('/')
def home():
    random_sentence = word_frequency.random_sentence()
    random_actor = word_frequency.random_actor()

    print('random actor = ', random_actor)
    print('random sentence ', random_sentence)
    return render_template('layout.html', sentence=random_sentence, actor=random_actor)
    # return word


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
