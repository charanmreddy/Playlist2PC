import requests
import json
import yt_dlp
import os
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "yt_dlp"])

if not os.path.exists("downloaded_songs.txt"):
    file = open("downloaded_songs.txt",'w')
    file.close()        

def download_audio(youtube_url):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'ffmpeg_location': r"Your Path to \ffmpeg\bin",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)

        # Delete these 4 lines of code , if you don't want the download logs to be printed
        audio_format = info.get('requested_downloads', [])[0]
        if audio_format:
            abr = audio_format.get('abr')
            ext = audio_format.get('ext')

API_KEY = 'Your_Youtube_Data_API_Key'
PLAYLIST_ID = 'Your_Playlist_ID'

url = 'https://www.googleapis.com/youtube/v3/playlistItems'

params = {
    'part': 'snippet',
    'playlistId': PLAYLIST_ID,
    'maxResults': 50,
    'key': API_KEY
}

k = open("downloaded_songs.txt",'r')
l = k.readlines()
k.close()
f = open("downloaded_songs.txt",'a')

nextPageToken = None

while True:
    if nextPageToken:
        params['pageToken'] = nextPageToken
    else:
        params.pop('pageToken', None)

    response = requests.get(url, params=params)
    data = response.json()

    for i in data["items"]:
        if f"{i['snippet']['title']},https://www.youtube.com/watch?v={i['snippet']['resourceId']['videoId']}\n" in l:
            print(f"{i['snippet']['title']}\nthere !\n")
        else:
            download_audio(f"https://www.youtube.com/watch?v={i['snippet']['resourceId']['videoId']}")
            f.write(f"{i['snippet']['title']},https://www.youtube.com/watch?v={i['snippet']['resourceId']['videoId']}\n")
            print(f"{i['snippet']['title']}\ndownloaded !\n")

    nextPageToken = data.get('nextPageToken')
    if not nextPageToken:
        break

f.close()