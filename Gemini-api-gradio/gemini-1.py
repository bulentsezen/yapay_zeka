import google.generativeai as genai
import gizliDosya

genai.configure(api_key=gizliDosya.api_key)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("3 kere 4 kaç eder")
print(response.text)