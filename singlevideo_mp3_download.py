# pip install pytube3

# if you get this error "urllib.error.HTTPError: HTTP Error 410: Gone" just upgrade your pytube
# python -m pip install --upgrade pytube

from pytube import YouTube
import os 

download_path = ""
yt = YouTube("https://www.youtube.com/watch?v=fZsUFpB3LzU")

ys = yt.streams.get_highest_resolution()
t = yt.streams.filter(only_audio=True).all()
out_file = t[0].download(download_path)

base, ext = os.path.splitext(out_file)
new_file =  base + '.mp3'
os.rename(out_file, new_file) 