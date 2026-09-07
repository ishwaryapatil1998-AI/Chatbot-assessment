import pyaudio
audio = pyaudio.PyAudio()
print('Available audio input devices:\n')
for i in range(audio.get_device_count()):
    info = audio.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:
        print(i, ':', info['name'])

audio.terminate()
import pyttsx3
def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()
print('🗣️ speech engine loaded successfully')
speak('Hello this is your personalized voice assistant how may i help you')
import speech_recognition as sr
recognizer = sr.Recognizer()
while True: 
    with sr.Microphone() as source:
        print("🎤Listening....")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio_data = recognizer.listen(source)
    print("Recording completed.")
    try:
        try:
            speech=recognizer.recognize_google(audio_data,language="en-IN")
            lang='English'
        except sr.UnknownValueError:
            speech=recognizer.recognize_google(audio_data,language="ta-IN")
            lang='Tamil'
        print(f"You asked in {lang}:",speech)
        speak("You asked:"+ speech)
        if speech.lower() in ["exit","quit","stop"]:
            speak("Goodbye Ishu shutting down assistant.")
            break
        try:
            import wikipedia
            summary = wikipedia.summary(speech, sentences=2)
            print("Answer:", summary)
            speak(summary)
        except Exception:
            speak("Sorry, I could not find an answer. But you said: " + speech)
    
    except sr.UnknownValueError:
        print("😔Sorry unable to hear you")
    except sr.RequestError as e:
        print("⚠️Speech recognition service error:",e)
