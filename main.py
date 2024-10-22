import requests
from bs4 import BeautifulSoup
from googletrans import Translator

url = "https://randomword.com/"

response = requests.get(url)

#Создаём функцию, которая будет получать информацию

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        #Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        #Получаем слово
        english_words = soup.find("div", id="random_word").text.strip()

        #Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Функция возвращает словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

#Создаем функцию перевода
def word_translator():
    translator = Translator()
    russian = translator.translate("english_words", dest="ru")
    russian_words = russian.text
    russian_definition = translator.translate("word_definition", dest="ru")
#    print("russian_words")
#    print("russian_definition")
    return {
        "russian_words": russian_words,
        "russian_definition": russian_definition
    }

#Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        russ_dict = word_translator()
        word = russ_dict.get("russian_words")
        word_definition = russ_dict.get("russian_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Верно!")
        else:
            print(f"Не угадал! Загадано слово {word}")

        play_again = input("Хотите сыграть еще? y/n: ")
        if play_again != "y":
            print("Игра окончена!")
            break

#Вызываем игровую функцию
word_game()