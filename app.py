from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Check if the form contains 'text' and 'language' keys
            if 'text' in request.form and 'language' in request.form:
                text = request.form['text']
                choice = int(request.form['language'])

                languages = {
                    1: 'en', 2: 'hi', 3: 'ta', 4: 'bn',
                    5: 'gu', 6: 'kn', 7: 'ml', 8: 'mr',
                    9: 'ne', 10: 'te', 11: 'ur'
                }

                if choice in languages:
                    lang_code = languages[choice]
                    tts = gTTS(text, lang=lang_code, slow=False)
                    audio_file = f'static/output.mp3'
                    tts.save(audio_file)
                    return render_template('index.html', audio_file=audio_file)
                else:
                    return render_template('index.html', error='Invalid Choice')

        except ValueError:
            return render_template('index.html', error='Invalid input. Please enter a valid integer choice.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
