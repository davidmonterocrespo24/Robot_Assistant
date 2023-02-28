import spacy
import speech_recognition as sr
import os
import random
from sklearn.naive_bayes import MultinomialNB

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load('es_core_news_sm')

# Entrenar el modelo Naive Bayes para la clasificación de texto
training_data = [
    ('¿Cuál es el clima hoy?', 'clima'),
    ('¿Qué hora es?', 'hora'),
    ('¿Cómo llego a la estación de tren?', 'direcciones'),
    ('Reproduce la canción "Bohemian Rhapsody"', 'reproducir'),
    ('¿Qué películas están en cartelera?', 'cine'),
    ('¿Cuál es la capital de Francia?', 'conocimiento'),
]
texts, labels = zip(*training_data)
nb = MultinomialNB()
nb.fit(texts, labels)

# Función para procesar la entrada de voz
def process_speech():
    # Inicializar el micrófono
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Di algo...')
        audio = r.listen(source)
    # Utilizar el reconocimiento de voz para transcribir la entrada de voz
    try:
        input_text = r.recognize_google(audio, language='es-ES')
        print('Has dicho:', input_text)
        return input_text
    except sr.UnknownValueError:
        print('Lo siento, no entendí lo que dijiste.')
    except sr.RequestError as e:
        print('Error en el servicio de reconocimiento de voz:', e)

# Función para procesar el texto de entrada y determinar la intención del usuario
def process_text(input_text):
    # Procesar el texto con spaCy
    doc = nlp(input_text.lower())
    # Identificar los verbos en el texto
    verbs = [token.lemma_ for token in doc if token.pos_ == 'VERB']
    # Determinar la intención del usuario utilizando el modelo Naive Bayes
    intent = nb.predict([input_text])[0]
    print('Intención:', intent)
    return intent

# Función para proporcionar una respuesta al usuario
def respond(intent):

    if intent == 'clima':
        # Obtener información sobre el clima utilizando una API
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
        print('Hoy el clima será soleado.')
    elif intent == 'hora':
        # Obtener la hora actual del sistema
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
        print('Son las 12:00.')
    elif intent == 'direcciones':
        # Utilizar una API de mapas para obtener direcciones a la estación de tren
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
        print('La estación de tren está a 5 minutos a pie.')
    elif intent == 'reproducir':
        # Utilizar una API de música
        print('Reproduciendo "Bohemian Rhapsody"...')
    elif intent == 'cine':
        # Obtener información sobre las películas en cartelera utilizando una API
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
        print('Las películas en cartelera son "El Rey León" y "Toy Story 4".')
    elif intent == 'conocimiento':
        # Buscar la respuesta en una base de datos o en una API de preguntas y respuestas
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
        print('La capital de Francia es París.')
    else:
        # Si la intención no se puede identificar, proporcionar una respuesta genérica
        responses = [
            'Lo siento, no entendí lo que dijiste.',
            'No estoy seguro de cómo responder a eso.',
            'Podrías reformular la pregunta, por favor.',
            'No tengo una respuesta para esa pregunta.'
        ]
        response = random.choice(responses)
        print(response)
        # Proporcionar una respuesta en voz alta utilizando la librería de síntesis de voz "espeak"
