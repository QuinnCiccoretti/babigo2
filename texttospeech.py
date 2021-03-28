import boto3
import uuid

# return a list of strings, audio file names
def makeAudioFiles(japanese_phrases):
  filenames = []
  for phrase in japanese_phrases:
    filename = japaneseTextToAudio(phrase['text'])
    filenames.append(filename)


# return an audio file name
def japaneseTextToAudio(japanese_text):
  polly = boto3.client('polly')
  res = polly.synthesize_speech( OutputFormat="mp3", SampleRate="22050", Text=japanese_text, VoiceId='Takumi')
  print(res)
  status = res['ResponseMetadata']['HTTPStatusCode']
  if status == 200:
      if "AudioStream" in res:
        with closing(res["AudioStream"]) as stream:
          rando_filename = uuid.v4() + ".mp3"
          writeAudio(rando_filename, stream)
          return rando_filename
      else:
        return 1
  else:
    return 1

def writeAudio( output_file, stream ):
  bytes = stream.read()
  try:
    with open(output_file, "wb") as file:
      file.write(bytes)
    if file.closed:
        print("\t==>", output_file, " is closed")
    else:
        print("\t==>", output_file, " is NOT closed")
  except IOError as error:
    print(error)
    sys.exit(-1)
