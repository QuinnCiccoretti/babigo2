from moviepy.editor import AudioFileClip, TextClip
#the japanese audio
def generateAudioClip(en, ja, audio_filename):
  print(audio_filename)
  audio = AudioFileClip(audio_filename)
  #TODO set duration or speed
  #start when the english started
  audio.set_start(en['start_time'])
  return audio
# a caption clip
def generateTextClip(en, ja):
  tc = TextClip(en['text'], color="white", align="North")
  tc.set_start(en['start_time'])
  return tc
