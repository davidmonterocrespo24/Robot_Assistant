from assistant import Assistant


assistant = Assistant(language_code="en-AU",
                      device_model_id="YOUR_MODEL_ID",
                      device_id="YOUR_DEVICE_ID")
while(True):
    assistant.assist()

        
 
    
    
    
print('Listening... Press Ctrl+C to exit')
