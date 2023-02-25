from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pyttsx3
import speech_recognition as sr


model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_response(model, tokenizer, input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    response_ids = model.generate(input_ids, max_length=1000, do_sample=True)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return ""

engine = pyttsx3.init()

while True:
    input_text = listen()
    if input_text:
        response_text = generate_response(model, tokenizer, input_text)
        print("Input: " + input_text)
        print("Response: " + response_text)
        engine.say(response_text)
        engine.runAndWait()