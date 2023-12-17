from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import VideoUnavailable
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
question = [
    inquirer.List("Video-Type",message="What Type Of Video You Wand To Download", choices=["Single Video", "Playlist"]),
]

usersChoice = inquirer.prompt(question, theme=GreenPassion())
print(usersChoice['Video-Type'])

a = usersChoice['Video-Type'].lower()

if a =='single video':
    yt = YouTube(input('\nEnter the URL of the video : '))
    try:
        yt.streams.get_highest_resolution().download()
    except VideoUnavailable:
        print(Fore.RED+"Video not available")
elif a =='playlist':
    pl = Playlist(input('\nEnter the URL of the playlist : '))
    for video in pl.videos:
        try:
            video.streams.get_highest_resolution().download()
        except VideoUnavailable:
            print(Fore.RED+"Video not available")
else:
    print('\nInvalid input')


