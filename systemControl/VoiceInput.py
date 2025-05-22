import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Говори что-нибудь...")

    #шумодав
    #recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = recognizer.listen(source)
            
            text = recognizer.recognize_google(audio, language='ru-RU')
            print(text)
        
        except sr.UnknownValueError:
            print("Не понял........")
        
        except sr.RequestError as e:
            print(f'Ошибка сервиса Google: {e}')
            break