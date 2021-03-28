import boto3
import uuid
from moviepy.editor import VideoFileClip
s3 = boto3.client('s3')

#return a video clip
def dlClip(inbucket, infile):
  localpath = "video/" + str(uuid.uuid4()) +".mp4"
  s3.download_file(inbucket, infile, localpath)
  c = VideoFileClip(localpath)
  c = c.volumex(0.5)
  return c
