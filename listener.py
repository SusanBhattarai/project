import speech_recognition as sr
import deepinfra

WIT_AI_KEY = "API KEY HERE" # https://wit.ai

recog = sr.Recognizer()
recog.pause_threshold = 1

def calibrate_for_ambient(duration: int):
    print("Calibrating for ambient noise.")
    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source, duration=duration)

def listen_to_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source=source)
        print("Finished Listening!")
        return audio
    
def transcribe(audio):
    try:
        transcribed_text = recog.recognize_wit(audio_data=audio, key=WIT_AI_KEY)
        print("User: ", transcribed_text)
        return transcribed_text
    except sr.UnknownValueError:
        print("Couldn't transcribe audio.")
        return False
    except sr.RequestError as error:
        print("Error sending request to Wit.ai")
        return False
    
calibrate_for_ambient(2)

audio = listen_to_audio()
transcribed_text = transcribe(audio)

if transcribed_text:
    llm_answer = deepinfra.get_result(transcribed_text)
    print("AI:   ", llm_answer)
else:
    print("Error getting result from LLM.")
