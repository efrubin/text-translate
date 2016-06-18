# translate.py
# Author: Elias Rubin
import requests
from config import *


def parse_body(body_text):
    """
        param: body_text :: string
    """
    try:
        split_text = body_text.rsplit(" ")
        source_lang = split_text[0]
        target_lang = split_text[1]
        query_string = " ".join(split_text[2:])

    except Exception:
        query_string = """Message not well formed. Message should be of form:
                            [source lang] [target lang] [query]"""
        source_lang = "la"
        target_lang = "en"

    return query_string, source_lang, target_lang


def query_translate_api(query_string, source_lang=None, target_lang=None):
    """
        param: query string :: string containing the text to translate
        param: source_lang :: string identifying the language to translate from
               english by default
        param: target_lang :: string indentifying the language to translate to
                spanish by default
        query the google translate API for a translation of the query string.
        returns a request.models.Response object
    """

    if source_lang is None:
        source_lang = 'en'
    if target_lang is None:
        target_lang = 'es'

    try:
        source_lang = LANGUAGES[source_lang]
    except KeyError:
        print "using user input source language: {}".format(source_lang)
        pass
    try:
        target_lang = LANGUAGES[target_lang]
    except KeyError:
        print "using user input target language: {}".format(target_lang)
        pass

    payload = {'key': GOOGLE_TRANSLATE_SECRET_KEY,
               'q': query_string,
               'source': source_lang,
               'target': target_lang}
    r = requests.get("https://www.googleapis.com/language/translate/v2?",
                     params=payload)
    return r


def translate(query_string, source_lang, target_lang):
    r = query_translate_api(query_string, source_lang, target_lang)
    print r
    try:
        translatedText = r.json()['data']['translations'][0]['translatedText']
    except Exception:
        translatedText = 'An error occured in the translation step.'
    return translatedText

# if __name__ == "__main__":
#     print translate("hello", "en","es")
