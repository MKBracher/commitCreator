import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import csv

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
# Create variables for storage of videos and videolinks
videoStore = []
youtubeURL = "https://www.youtube.com/watch?v="
videoURL = ""
count = 0
for item in response['items']:
    videoURL = youtubeURL + item['id']
    videoStore.append({'channelTitle': item['snippet']['channelTitle'], 
    'videoTitle': item['snippet']['title'], 'viewCount': item['statistics']['viewCount'],
    'URL': videoURL})
    # print(videoStore[count])
    count += 1

# Check if file has been written to
fileSize = os.path.getsize("saved.csv")

# Write to file and add the headers
if fileSize == 0:
    with open('saved.csv', mode='w', encoding="utf-8") as csv_file:
        fieldnames = ['channelTitle', 'videoTitle', 'viewCount', 'URL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # Add each saved video to the csv file.
        count = 0
        for item in videoStore:
            writer.writerow(videoStore[count])
            count += 1

# Append to file 
else:
    with open('saved.csv', mode='a', encoding="utf-8") as csv_file:
        fieldnames = ['channelTitle', 'videoTitle', 'viewCount', 'URL']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Add each saved video to the csv file.
        count = 0
        for item in videoStore:
            writer.writerow(videoStore[count])
            count += 1

