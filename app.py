from flask import Flask, render_template
import os
import word_frequency
import cleanup
from word_frequency import Dictogram

app = Flask(__name__)


@app.route('/')
def home():
    # Get cleaned data
    file_name = 'SiliconValley.txt'
    cleaned_file = cleanup.clean_file(file_name)

    # Create data structure
    data_structure = Dictogram(cleaned_file)

    # Pass data structure to get random setence
    random_sentence = word_frequency.random_sentence(data_structure)

    # Get a random actor to say the quote
    random_actor = word_frequency.random_actor()
    random_actor_cleaned = random_actor.replace(' ', '_')
    random_actor_cleaned = random_actor_cleaned.replace('\'', '')
    print('random actor = ', random_actor)
    print('random actor cleaned ', random_actor_cleaned)
    print('random sentence ', random_sentence)

    # Render that website <3
    return render_template('layout.html', sentence=random_sentence, actor=random_actor, actor_image=random_actor_cleaned)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
