from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import send_from_directory
import os
from gtts import gTTS
import brain
from time import * 
import speech_recognition as sr
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')
def messageRecived():
  print( 'message was received!!!' )

def capture():

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        audio = rec.listen(source, phrase_time_limit=5)
    text = rec.recognize_google(audio, language='en-US')
    return text

@socketio.on( 'my events' )
def handle_my_custom_event1( json1 ):
  # message=capture()
	message = json1['message']
	answer=brain.chat(message)
	json1['answer'] = answer
	json1['bot']='Chatter'
	print( 'Event Details : ' + str(json1))
	# speech = tts(text=answer, lang='en')
	# speech_file = 'response.mp3'
	# speech.save(speech_file)
	socketio.emit( 'my response', json1, callback=messageRecived() )
	# sound = AudioSegment.from_mp3(speech_file)
	# play(sound)
	# os.remove(speech_file)

if __name__ == '__main__':
  socketio.run( app, debug = True )
