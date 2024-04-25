# CoPilot (python ile sesi yazıya dönüştüren program yaz)
# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr

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
