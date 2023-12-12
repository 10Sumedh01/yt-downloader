from pytube import YouTube
from pytube import Playlist

a = input('\nEnter "S" for single video or "P" for playlist : ').lower()
print(a)

if a =='s':
    yt = YouTube(input('\nEnter the URL of the video : '))
    yt.streams.get_highest_resolution().download()
elif a =='p':
    pl = Playlist(input('\nEnter the URL of the playlist : '))
    for video in pl.videos:
        video.streams.get_highest_resolution().download()
else:
    print('\nInvalid input')
