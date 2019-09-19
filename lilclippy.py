from googlesearch import search
import speech_recognition as sr



r = sr.Recognizer()


mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    transcript = r.recognize_google(audio)
    print(transcript)

transcript = query

for j in search(query, tld="co.us", num=10, stop=1, pause=3):
    print(j)
    

