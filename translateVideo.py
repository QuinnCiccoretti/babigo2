import argparse
from speechtotext import makeTranscript
from englishphraser import getEnglishPhrases
from translateTextToText import translateEnglishPhrases
from texttospeech import makeAudioFiles
from clipMaker import generateAudioClip, generateTextClip 
from pullClip import dlClip
from moviepy.editor import CompositeVideoClip, CompositeAudioClip
import json
# Get the command line arguments and parse them
parser = argparse.ArgumentParser( prog='translatevideo.py', description='Process a video found in the input file, process it, and write it out to the output file')
# parser.add_argument('-region', required=True, help="The AWS region containing the S3 buckets" )
parser.add_argument('-inbucket', required=True, help='The S3 bucket containing the input file')
parser.add_argument('-infile', required=True, help='The input file to process')
parser.add_argument('-outbucket', required=True, help='The S3 bucket for output')
parser.add_argument('-outfilename', required=True, help='The mp4 file name for output')

args = parser.parse_args()

transcript = makeTranscript(args.inbucket, args.infile)
# print(json.dumps(transcript, indent=4))
print(transcript)
english_phrases = getEnglishPhrases(transcript)
print(english_phrases)
japanese_phrases = translateEnglishPhrases(english_phrases)
print(japanese_phrases)
audio_filename_list = makeAudioFiles(japanese_phrases)
print(audio_filename_list)

n_phrases = len(english_phrases)
audioClips = []
captionClips = []
for i in range(0, n_phrases):
  en = english_phrases[i]
  ja = japanese_phrases[i]
  audio_filename = audio_filename_list[i]
  audioClips.append(generateAudioClip(en, ja, audio_filename))
  captionClips.append(generateTextClip(en, ja))

og = dlClip(args.inbucket, args.infile)
allvids = [og]
allvids.extend(captionClips)
video = CompositeVideoClip(allvids)

for clip in audioClips:
    print(clip.start)
sound = CompositeAudioClip(audioClips)
print("OG duration: " + str(og.duration))
sound = sound.set_duration(og.duration)
video = video.set_duration(og.duration)
video = video.set_audio(sound)

video.write_videofile("output/"+args.outfilename)
