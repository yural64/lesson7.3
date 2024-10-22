from googletrans import Translator

translator = Translator()
result = translator.translate("dog", dest="ru")
print(result.text)