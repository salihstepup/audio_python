import speech_recognition as sr
##from guessing game im port recognize speech from mic
r=sr.Recognizer()
with sr.Microphone() as source:
    print("say any thing")
    audio=r.listen(source)
    print("timeover")
    
try:
     print("text:"+r.recognize_google(audio))
except:
     pass
