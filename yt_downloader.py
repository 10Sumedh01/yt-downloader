from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import VideoUnavailable
from pytube.cli import on_progress
from colorama import Fore
import pyfiglet
import inquirer
from inquirer.themes import GreenPassion




#Display Header
f = pyfiglet.Figlet(font="ogre", width=80)
x = (f.renderText('    YT Downloader'))
print(Fore.YELLOW+'      ----------------------------------------------------------------')
print(Fore.RED+ x)
print(Fore.YELLOW+'      ----------------------------------------------------------------') 

#Logic Part
# def progress_function(video_stream, total_size, bytes_remaining):
#     total_size = video_stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percent = (bytes_downloaded / total_size)*100
#     print('\r'+"▌" * int(percent)+ " " * (100-int(percent))+ "{}%".format(int(percent)),end='')

# def getAllLinks(playList):
#     allLinks = []
#     youtubeLink = 'https://www.youtube.com'
#     pl = Playlist(playList)
#     for linkprefix in pl.parse_links():
#         allLinks.append(youtubeLink + linkprefix)
#     return allLinks

# def downloadPlaylist(playlistLink):
#     linkArray = getAllLinks(playlistLink)
#     for link in linkArray:
#         downloadVideo(link)

question = [
    inquirer.List("Video-Type",message="What Type Of Video You Wand To Download", choices=["Single Video", "Playlist"]),
]

usersChoice = inquirer.prompt(question, theme=GreenPassion())
print(usersChoice['Video-Type'])

a = usersChoice['Video-Type'].lower()

if a =='single video':
    yt = YouTube(input(Fore.YELLOW+'\nEnter the URL of the video : '),on_progress_callback=on_progress)
    try:
        yt.streams.get_highest_resolution().download("Videos")
    except VideoUnavailable:
        print(Fore.RED+"Video not available")
elif a =='playlist':
    pl = Playlist(input(Fore.YELLOW+'\nEnter the URL of the playlist : '))
    for video in pl.videos:
        try:
            # video.streams.get_highest_resolution().download("Videos")
            print(video)
        except VideoUnavailable:
            print(Fore.RED+"Video not available")
else:
    print(Fore.RED+'\nInvalid input')


