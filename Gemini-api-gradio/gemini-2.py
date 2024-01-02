import google.generativeai as genai
import gizliDosya
import gradio as gr

genai.configure(api_key=gizliDosya.api_key)

model = genai.GenerativeModel('gemini-pro')

def generate(prompt):
    cevap = model.generate_content(prompt)
    return cevap.text

title = ' Yapay Zeka Sohbet'
description = 'Google yapay zekaya soralım.'

gr.Interface(fn=generate, inputs=["text"], outputs=["text"],
             title=title, description=description,
             # Set theme and launch parameters
             theme='finlaymacklon/boxy_violet').launch(server_port=8080, share=True)