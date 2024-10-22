import requests
from bs4 import BeautifulSoup

url = "https://randomword.com/"

response = requests.get(url)

print(response.text)

#Создаём функцию, которая будет получать информацию

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        print(response.text)

        #Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")

        #Получаем слово
        english_words = soup.find_all("div", id="random_word")

        #Получаем описание слова
        word_definition = soup.find_all("div", id="random_word_definition")

        # Функция возвращает словарь
        return {
            "english_words",
            "word_definition"
        }
    except:
        print("Произошла ошибка")
        