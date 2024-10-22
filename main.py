import requests
from bs4 import BeautifulSoup

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
            "english_words",
            "word_definition"
        }
    except:
        print("Произошла ошибка")

#Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово?")
        if user == word:
            print("Верно!")
        else:
            print(f"Не угадал! Загадано слово {word}")

        play_again = input("Хотите сыграть еще? y/n:")
        if play_again != "y":
            print("Игра окончена!")
            break

#Вызываем игровую функцию
word_game()