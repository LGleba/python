# 2020
# Translator from Yandex
# Powered by LGleba


import requests


def translate(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'API FROM YANDEX'
    TEXT = text
    LANG = lang

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})

    return eval(r.text)


""" Example
print(translate("Hello", "ru")["text"][0])
"""