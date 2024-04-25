# pip install gTTS
# pip install pygame
# https://github.com/bulentsezen/yolov4/blob/main/sesliOkuma.py
# Video: Yolov4 ile tanınan nesne isimlerini gTTS ile sesli olarak okutma:
# Linki: https://www.youtube.com/watch?v=nwDkK8Is9cQ&t=0s

import google.generativeai as genai
import gizliDosya
import speech_recognition as sr
from pygame import mixer  # Load the pygame library
import time
from gtts import gTTS

genai.configure(api_key=gizliDosya.api_key)

# Mikrofonu başlat
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Bir şey söyleyin:")
    audio = r.listen(source)

try:
    # Ses tanıma işlemi
    recognized_text = r.recognize_google(audio, language='tr-TR')
    print("Söylediğiniz: " + recognized_text)
except sr.UnknownValueError:
    print("Ses anlaşılamadı.")
except sr.RequestError as e:
    print(f"Hata: {e}")

# Gemini soruyu sor, cevabı yazdır
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(recognized_text)
print(response.text)

soru_cevap = "cevap" + response.text

# gTTS ile Gemini cevabını sesli okuma
tts = gTTS(soru_cevap, lang="tr")
tts.save("mrb.mp3")

mixer.init()
mixer.music.load('mrb.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)