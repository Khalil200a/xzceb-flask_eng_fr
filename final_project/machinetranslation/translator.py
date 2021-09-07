"""System module."""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()


authenticator = IAMAuthenticator("-Grq2z9zJ7pruOoCsqBqaXukkHYkNjUsZYJ4oUL7IfH8")
language_translator = LanguageTranslatorV3(
    version='2019-04-30',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/538ad240-7cb5-48ca-9d96-5223a7b588a4")


def englishToFrench(englishText):
    """translate from english to frensh"""
    frenchtranslation = language_translator.translate(
        text=englishText,
        model_id="en-fr"
    ).get_result()
    frenchText = frenchtranslation.get("translations")[0].get("translation")
    return frenchText

def frenchToEnglish(frenchText):
    """translato from french to english"""
    englishtranslation = language_translator.translate(
        text=frenchText,
        model_id="fr-en"
    ).get_result()
    englishText = englishtranslation.get("translations")[0].get("translation")
    return englishText
