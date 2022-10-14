from gtts import gTTS #gTTS가 크기 때문에 gTTS에서 필요한 것만 가져옴
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = '안녕하세요. 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다.'
tts = gTTS(text = text, lang = 'ko')

current_file_path = os.getcwd() + "./hi.mp3"
tts.save(current_file_path)

playsound(current_file_path)