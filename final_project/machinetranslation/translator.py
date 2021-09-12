'''Functions for translating english to french and vice versa.'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION_LT,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translates english text to french text.'''
    if english_text == "":
        return ""
    french_text_dict = language_translator.translate(\
        text=english_text, model_id='en-fr')
    french_text = french_text_dict.get_result()['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Translates french text to english text.'''
    if french_text == "":
        return ""
    english_text_dict = language_translator.translate(\
        text=french_text, model_id='fr-en')
    english_text = english_text_dict.get_result()['translations'][0]['translation']
    return english_text
