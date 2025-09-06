import speech_recognition as sr
import subprocess
import webbrowser
import pyowm

# Создаем объект для распознавания речи
recognizer = sr.Recognizer()

owm = pyowm.OWM('5817d6a145c443107efc34417e35c2ac')

def voce_input():
    # Используем микрофон в качестве источника звука
    with sr.Microphone() as source:
        print("Скажи что-нибудь...")  
        # Слушаем звук с микрофона
        audio = recognizer.listen(source)
    # Возвращаем записанный аудиообъект
    return audio





def conet_text(audio):
    try:
        # Преобразуем речь в текст с помощью Google Speech Recognition
        # language="uk-UA" означает украинский язык
        text = recognizer.recognize_google(audio, language="uk-UA")
        print("Ти сказав: " + text)
    except sr.UnknownValueError:
        # Ошибка, если речь не распознана
        text = ""
        print("Я не зрозумів, що ти сказав")
    except sr.RequestError:
        # Ошибка подключения к сервису Google
        text = ""
        print("Помилка підключення до сервісу розпізнавання")
    # Возвращаем результат (строку с текстом или пустую строку)
    return text

def process_voice_command(text):
    if "привіт" in text.lower():
        print("привіт як справи")
    elif "я справи" in text.lower():
        print("супер")
    elif "відкрий калькулятор" in text.lower():
        subprocess.call(['calc'])
    elif "roblox" in text.lower():
        subprocess.call(['C:/Users/LOGIKA/AppData/Local/Roblox/Versions/version-c1ac69007bdc4e48/RobloxPlayerBeta.exe'])
    elif "youtube" in text.lower():
        webbrowser.open("https://www.youtube.com/?app=desktop&gl=UA&hl=uk")
    elif "лололошка" in text.lower():
        webbrowser.open("https://www.youtube.com/@MrLololoshka")
    elif "танки" in text.lower():
        webbrowser.open("https://www.wargaming.net/en")
    elif "github" in text.lower():
        webbrowser.open("https://github.com/")
    elif "зз" in text.lower():
        webbrowser.open("https://emupedia.net/beta/emuos/")
    elif "погода" in text.lower():
        place = text.lower()[7:]
        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather2 = "температура (грфдусицельсий)" + str(int(weather.temperature("celsius")["temp"])) + "\n"
        print(weather2)


def main():
    # Получаем аудио с микрофона
    audio = voce_input()
    # Пробуем распознать его в текст
    text = conet_text(audio)
    process_voice_command(text)



# Точка входа в программу
if __name__ == "__main__":
    main()