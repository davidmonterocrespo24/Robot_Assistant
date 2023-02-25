from assistant_con_animation import Assistant
from animation import Animation

a = Animation(1)
a.run()
assistant = Assistant(language_code="en-AU")
assistant.start()
print('Listening... Press Ctrl+C to exit')
