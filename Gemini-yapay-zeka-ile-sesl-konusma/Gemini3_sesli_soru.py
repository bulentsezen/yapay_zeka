import google.generativeai as genai
import gizliDosya
import speech_recognition as sr

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

# Gemini soruyu sor
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(recognized_text)
print("cevap: ", response.text)