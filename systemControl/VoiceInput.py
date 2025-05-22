import speech_recognition as sr

# Создаём распознаватель
recognizer = sr.Recognizer()

# Используем микрофон
with sr.Microphone() as source:
    print("🎤 Говори что-нибудь...")

    # Настроим шумоподавление
    #recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            # Слушаем
            audio = recognizer.listen(source)
            
            # Преобразуем речь в текст
            text = recognizer.recognize_google(audio, language='ru-RU')
            print("👂 Ты сказал:", text)
        
        except sr.UnknownValueError:
            print("😕 Не понял, повтори...")
        
        except sr.RequestError as e:
            print(f"❌ Ошибка сервиса Google: {e}")
            break