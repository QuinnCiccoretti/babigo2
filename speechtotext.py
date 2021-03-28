import boto3
import requests
import json
import uuid
import time
# transcribe given an s3 file
def makeTranscript( bucket, mediaFile ):
  transcribe = boto3.client('transcribe')
  
  mediaUri = "https://s3-us-east-1.amazonaws.com/" + bucket + mediaFile 
  job_name = "transcribe_" + uuid.uuid4().hex + "_" + mediaFile
  
  response = transcribe.start_transcription_job( TranscriptionJobName= job_name, \
    LanguageCode = "en-US", \
    MediaFormat = "mp4", \
    Media = { "MediaFileUri" : mediaUri }, \
    )
  
  not_done = True
  while( not_done):
    print( "."),
    time.sleep( 3 )
    response = transcribe.get_transcription_job( TranscriptionJobName=job_name )
    not_done = response["TranscriptionJob"]["TranscriptionJobStatus"] == "IN_PROGRESS"

  transcriptURI = str(response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"])
  transcript = requests.get(transcriptURI)
  return json.loads(transcript.text)
