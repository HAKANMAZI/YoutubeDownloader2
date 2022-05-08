# pip install pytube3

# if you get this error "urllib.error.HTTPError: HTTP Error 410: Gone" just upgrade your pytube
# python -m pip install --upgrade pytube

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=fZsUFpB3LzU")

ys = yt.streams.get_highest_resolution()
ys.download()