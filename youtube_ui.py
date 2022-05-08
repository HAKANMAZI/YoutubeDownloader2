import tkinter as tk 
import tkinter.scrolledtext as st 
from tkinter import filedialog
import youtube_downloader as yd

root = tk.Tk() 
root.title("Youtube Video Downloader")

# Title Label 
tk.Label(root,text = "Youtube Downlaoder", font = ("Times New Roman", 12),  
            background = 'green', foreground = "white").grid(column = 1,row = 0)            
tk.Label(root,text = "Playlist linki girin: ", font = ("Times New Roman", 12)).grid(column = 0,row = 1) 


#get playlist link
entry1 = tk.Entry(root) 
entry1.grid(column = 1,row = 1)


#text_area
text_area = st.ScrolledText(root, width = 50,  height = 8, font = ("Times New Roman",12)
                            ).grid(column = 1, pady = 10, padx = 10)


def get_mp3():
    playlist = entry1.get()
    print(playlist)
    folder_path = filedialog.askdirectory()
    print(folder_path)
    yd.get_youtube_mp3(playlist, folder_path)
    
button3 = tk.Button(root, text=" MP3 downloader ", command=get_mp3)
button3.grid( sticky="nsew")


def get_mp4():
    playlist = entry1.get()
    print(playlist)
    folder_path = filedialog.askdirectory()
    print(folder_path)
    yd.get_youtube_mp4(playlist, folder_path)
    
button2 = tk.Button(root, text=" M4 downlaoder", command =get_mp4)
button2.grid(  sticky="nsew")



root.mainloop()