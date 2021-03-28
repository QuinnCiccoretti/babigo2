import argparse
from speechtotext import makeTranscript
from englishphraser import getEnglishPhrases
from translateTextToText import translateEnglishPhrases
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
