import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version_lt,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    if englishText == "":
        return ""
    frenchTextDict = language_translator.translate(\
        text=englishText, model_id='en-fr')
    frenchText = frenchTextDict.get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    if frenchText == "":
        return ""
    englishTextDict = language_translator.translate(\
        text=frenchText, model_id='fr-en')
    englishText = englishTextDict.get_result()['translations'][0]['translation']
    return englishText
