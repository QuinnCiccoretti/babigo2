from moviepy.editor import AudioFileClip, TextClip
#the japanese audio
def generateAudioClip(en, ja, audio_filename):
  delta_t = en['end_time'] - en['start_time']
  audio = AudioFileClip(audio_filename)
  #TODO set duration or speed
  #start when the english started
  audio = audio.set_start(en['start_time'])
  return audio
# a caption clip
def generateTextClip(en, ja):
  delta_t = en['end_time'] - en['start_time']
  print(delta_t)
  tc = TextClip(en['text'], color="white", align="North")
  tc = tc.set_start(en['start_time'])
  return tc
