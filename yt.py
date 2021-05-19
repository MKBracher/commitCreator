import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

api_key = os.environ['api_key']

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
    part="id, statistics, snippet",
    chart = "mostPopular",
    regionCode='AU',
)

response = request.execute()

# print(response)
videoStore = []
youtubeURL = "https://www.youtube.com/watch?v="
videoURL = ""
count = 0

for item in response['items']:
    videoURL = youtubeURL + item['id']
    videoStore.append({'channelTitle': item['snippet']['channelTitle'], 
    'videoTitle': item['snippet']['title'], 'viewCount': item['statistics']['viewCount'],
    'URL': videoURL})
    count += 1






