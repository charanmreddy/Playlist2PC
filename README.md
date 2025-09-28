<h1 align="center">Playlist2PC</h1>
<p align="center">Python script that automatically downloads all songs from a YouTube playlist to your local machine. It checks for existing downloads and downloads any new additions to to the playlist , each time you run the code .</p></p><br><br><br>

# Introduction

**Download Songs/audio from The Public Youtube Playlist of your choice with a click .**\
Uses Google's YouTube Data API v3 , to fetch playlist details\
[yt-dlp](https://github.com/yt-dlp/yt-dlp) is used to download files.\
Files are downloaded to your _current working directory_.\
<br><br><br>

# Usage

Clone this repo .
```git clone https://github.com/charanmreddy/Playlist2PC.git```
enter the repo
```cd Playlist2PC```

Download the requirements (requests , yt_dlp)
```pip install -r requirements.txt```
<br><br>
### Downloading ffmpeg

This step is a must for the script to extract audio and convert to formats.

1. Download the zip file from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).
2. Extract the contents to your desired path , and copy the path of \ffmpeg\bin
3. Paste it for `ffmpeg_location` parameter .
<br><br>
### Playlist ID

The Playlist ID is a string , that refers to your YT Playlist .

If you open a youtube Playlist on a browser , the marked part is the Playlist ID  
![Example ID](images/plid.png)  
It starts with **PL** and looks something like this :
> PL08Qukwx7nDvSR7B8RgvfGZIbOd7T0wPu

Paste it for the variable `PLAYLIST_ID` in the code .

[IMPORTANT]
> Make sure The Playlist's visibility is set to public .
<br><br>
### YouTube API

This Provides us with data about the Playlist

To Get your API :

1. Visit [Google API Library](https://console.cloud.google.com/apis/dashboard)
2. Select **Enable APIs and services**
3. Find and select **Select Youtube Data API v3**
4. Create API , copy your API_KEY and paste it for `API_KEY` variable in the code

<br><br><br>
# Final Notes

Run the code manually , _ideally once a day_.

You can tweak the format , quality etc by changing parameters and calls . For more information [visit](https://github.com/yt-dlp/yt-dlp).

[NOTE]
> In case of a HTTPS error : Youtube changes its structure very frequently , and so changes are pushed to yt_dlp . Run `pip -m install -U yt_dlp` for the latest version .

