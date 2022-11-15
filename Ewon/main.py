import snowboydecoder
import sys
import signal
import time
import logging
from assistant import Assistant

interrupted = False

logging.basicConfig()
logger = logging.getLogger("daemon")
logger.setLevel(logging.DEBUG)



def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


signal.signal(signal.SIGINT, signal_handler)



assistant = Assistant(language_code="en-AU",
                      device_model_id="YOUR_MODEL_ID",
                      device_id="YOUR_DEVICE_ID")
while(True):
    assistant.assist()

        
 
    
    
    
print('Listening... Press Ctrl+C to exit')
