from googletrans import Translator

translator = Translator()
text_translated = translator.translate("hello world", src='en', dest='hi')
print(text_translated.text)