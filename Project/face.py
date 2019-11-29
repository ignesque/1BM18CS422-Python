from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import send_from_directory

# import pyttsx3
# from gtts import gTTS
import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS as tts
import brain
from time import * 
app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my events' )
def handle_my_custom_event1( json1 ):
  message = json1['message']
  if message != '':
    answer=brain.chat(message)
    json1['answer'] = answer
    json1['bot']='Chatter'
    socketio.emit( 'my response', json1, callback=messageRecived() )
    print( 'Event Details : ' + str(json1))
    # speech = tts(text=answer, lang='en')
    # speech_file = 'response.mp3'
    # speech.save(speech_file)
    tts = gTTS(text=answer, lang='en', slow=False) 
    myobj.save("response.mp3")
    os.system("mpg321 response.mp3") 
    # sound = AudioSegment.from_mp3(speech_file)
    # play(sound)
    # os.remove(speech_file)

if __name__ == '__main__':
  socketio.run( app, debug = True )
