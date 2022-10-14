from gtts import gTTS #gtts가 크기 때문에, gtts패키지에서 gTTS모듈만을 가져옴
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = '안녕하세요. 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다.'
tts = gTTS(text = text, lang = 'ko')

current_file_path = os.getcwd() + "./hi.mp3"
tts.save(current_file_path)

playsound(current_file_path) #실행 후 vscode에서 TTS읽음.