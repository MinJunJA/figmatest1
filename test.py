from playsound import playsound
from gtts import gTTS

tutorial="upload.mp3"
name_tts = gTTS(text="잠시만 기다려주세요.", lang="ko")
name_tts.save(tutorial)

playsound()