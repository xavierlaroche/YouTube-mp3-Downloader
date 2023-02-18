# First Python project - Started on 2023/03/16
# TODO Create GUI and make it pretty (pyQt)
# TODO Wrap it in a friendly usable app



# Imports
import os
from pytube import YouTube

# Download
yt = YouTube(str(input("Enter the URL: ")))
print("Downloading " + yt.title)
yt.streams.get_audio_only().download(output_path="/Users/xavierlaroche/downloads")

# Convert mp4 tp mp3
old_name = "/Users/xavierlaroche/downloads/" + yt.title + ".mp4"
new_name = "/Users/xavierlaroche/downloads/" + yt.title + ".mp3"
os.rename(old_name, new_name)