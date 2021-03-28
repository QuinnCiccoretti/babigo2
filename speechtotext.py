import boto3
import requests

# transcribe given an s3 file
def makeTranscript( bucket, mediaFile ):
  transcribe = boto3.client('transcribe')
  
  mediaUri = "https://s3-us-east-1.amazonaws.com/" + bucket + mediaFile 
  
  response = transcribe.start_transcription_job( TranscriptionJobName="transcribe_" + uuid.uuid4().hex + "_" + mediaFile , \
    LanguageCode = "en-US", \
    MediaFormat = "mp4", \
    Media = { "MediaFileUri" : mediaUri }, \
    )
  
  while( response["TranscriptionJob"]["TranscriptionJobStatus"] == "IN_PROGRESS"):
    print( "."),
    time.sleep( 3 )
    response = getTranscriptionJobStatus( response["TranscriptionJob"]["TranscriptionJobName"] )

  transcriptURI = str(response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"])
  transcript = requests.get(transcriptURI)
  return transcript.text