import argparse
from speechtotext import makeTranscript
# Get the command line arguments and parse them
parser = argparse.ArgumentParser( prog='translatevideo.py', description='Process a video found in the input file, process it, and write tit out to the output file')
# parser.add_argument('-region', required=True, help="The AWS region containing the S3 buckets" )
parser.add_argument('-inbucket', required=True, help='The S3 bucket containing the input file')
parser.add_argument('-infile', required=True, help='The input file to process')
# parser.add_argument('-outbucket', required=True, help='The S3 bucket containing the input file')
# parser.add_argument('-outfilename', required=True, help='The file name without the extension')
# parser.add_argument('-outfiletype', required=True, help='The output file type.  E.g. mp4, mov')
# parser.add_argument('-outlang', required=True, nargs='+', help='The language codes for the desired output.  E.g. en = English, de = German')    
args = parser.parse_args()

transcript = makeTranscript(args.inbucket, args.infile)
print(transcript)
