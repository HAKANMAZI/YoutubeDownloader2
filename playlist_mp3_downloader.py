# pip install selenium==4.1.5 
# pip install webdriver-manager==3.5.4

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytube import YouTube 
import os

playlist = "https://www.youtube.com/watch?v=snmAu25tqMw&list=RDCLAK5uy_n1j1GACZO4o7U1m708pa7jV1q7zR-cY44&start_radio=1"
download_path = ""


def get_youtube_mp3(playlist,download_path):
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.get(playlist)

    lists = []
    for a in wd.find_elements_by_xpath('.//a'):
        lists.append(a.get_attribute('href'))

    matching = [s for s in lists if "watch?v" in str(s)]
    mylist = list(set(matching))

    error_link =[]
    for x,a in enumerate(mylist):
        print(str(x) +": "+ a)
        try:
            yt = YouTube(a)
            t = yt.streams.filter(only_audio=True).all()
            out_file = t[0].download(download_path)

            base, ext = os.path.splitext(out_file)
            new_file =  base + '.mp3'
            os.rename(out_file, new_file) 
        except:
            print("Error: "+ str(x))
            error_link.append(a)

    for b in error_link:
        print(b)


get_youtube_mp3(playlist,download_path)