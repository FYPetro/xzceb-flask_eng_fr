"""Provides translation between English and French"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core.api_exception import ApiException

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(f"{apikey}")
language_translator = LanguageTranslatorV3(
    version=f"{VERSION}",
    authenticator=authenticator
)

language_translator.set_service_url(f"{url}")

def english_to_french(englishtext):
    """Translates a string from English to French"""
    frenchtext = ""
    try:
        response = language_translator.translate(
            text=englishtext,
            model_id='en-fr').get_result()
        frenchtext = response['translations'][0]['translation']
    except ApiException:
        pass
    return frenchtext

def french_to_english(frenchtext):
    """Translates a string from French to English"""
    englishtext = ""
    try:
        response = language_translator.translate(
            text=frenchtext,
            model_id='fr-en').get_result()
        englishtext = response['translations'][0]['translation']
    except ApiException:
        pass
    return englishtext
