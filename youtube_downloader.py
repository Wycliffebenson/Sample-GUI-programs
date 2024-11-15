#!pip install yt_dlp
#pip install colorama
import yt_dlp

from colorama import *
init(autoreset=True)
 
print(Fore.GREEN + "YOUTUBE VIDEO DOWNLOADER😎")

url = input("Enter the video url: ")
ydl_opts = { }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print( Fore.GREEN + "Video Downloaded Successfully!")