from flask import Flask, render_template, request, redirect
import os
import word_frequency
import cleanup
import markov
import twitter


app = Flask(__name__)


@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


@app.route('/')
def home():
    # Get cleaned data
    file_name = 'SiliconValley.txt'
    cleaned_file = cleanup.clean_file(file_name)

    # Create data structure
    data_structure = markov.make_higher_order_markov_model(3, cleaned_file)
    print data_structure

    # Pass data structure to get random setence with 140 chars
    random_sentence = markov.generate_random_sentence_n(140, data_structure)

    # Get a random actor to say the quote
    random_actor = word_frequency.random_actor()
    random_actor_cleaned = random_actor.replace(' ', '_')
    random_actor_cleaned = random_actor_cleaned.replace('\'', '')
    print('random actor = ', random_actor)
    print('random actor cleaned ', random_actor_cleaned)
    print('random sentence ', random_sentence)

    # Render website <3
    return render_template('layout.html', sentence=random_sentence, actor=random_actor, actor_image=random_actor_cleaned)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
