from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import json


# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
@app.route('/')
def index_page():
    return "Hello world"

@app.route('/id/<video_id>', methods=['GET', 'POST'])
def get_transcript(video_id):
    transcript = ""
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

    for i in transcript_list:
        transcript += " " + i.get('text')

    return transcript
# server the app when this file is run
if __name__ == '__main__':
    app.run(debug=True)