import boto3
from englishphraser import newPhrase
def translateEnglishPhrases( english_phrases ):
  #set up the Amazon Translate client
  translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
  translated_phrases = []
  for phrase in english_phrases:
    t = newPhrase()
    t['start_time'] = phrase['start_time']
    t['end_time'] = phrase['end_time']
    res = translate.translate_text(Text=phrase['text'],SourceLanguageCode="en", TargetLanguageCode="ja")
    t['text'] = res['TranslatedText']
    translated_phrases.append(t)  
  return translated_phrases
