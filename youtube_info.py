# pip install pytube3

# if you get this error "urllib.error.HTTPError: HTTP Error 410: Gone" just upgrade your pytube
# python -m pip install --upgrade pytube

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=fZsUFpB3LzU")


print("Title: ",yt.title) #Title of video
print("Number of views: ",yt.views) #Number of views of video
print("Length of video: ",yt.length,"seconds") #Length of the video
print("Description: ",yt.description) #Description of video
print("Ratings: ",yt.rating) #Rating


#printing all the available streams
print(yt.streams)

# let’s filter out audio-only streams. 
print(yt.streams.filter(only_audio=True))

# let’s filter out video-only streams.
print(yt.streams.filter(only_video=True))



ys = yt.streams.first()
ys.download()
ys.download('location')