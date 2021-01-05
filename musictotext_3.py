# Made by Ray


# for getting music metadata
from tinytag import TinyTag

# for navigating file folders, etc.
import glob, os

# for doing quick searches
import re

from bs4 import BeautifulSoup
from html import unescape

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

playlists = []

# Top-level folder where all playlists and songs are stored
topdir = "D:\\Libraries\\Music\\"
os.chdir(topdir)

# saves all playlist files into a list
for path, dirs, files in os.walk(topdir):
    for file in files:
        if file.endswith('.wpl'):
            playlists.append(os.path.join(path, file))



# goes through each playlist and finds files
for playlist in playlists:
    playlistname = playlist[playlist.rfind('\\')+1:playlist.find('.wpl')]
    print('\n\n' + playlistname
        + '\n~~~~~~~~~~~~~')
    content = open(playlist, 'r', encoding='utf-8').read()
    quotes = []

    numsongs = 0

    with open(playlistname+".txt", 'w') as writefile:
        for quote in re.finditer('"', content):
            quotes.append(quote)
        for i in range(len(quotes)-1):
            if "media src" in content[quotes[i].start()-15:quotes[i].start()]:
                track = content[quotes[i].start()+1:quotes[i+1].start()]
                track = BeautifulSoup(unescape(track), 'lxml')
                try:
                    if ":" not in track.text:
                        tag = TinyTag.get( playlist[0:playlist.rfind('\\')+1] + track.text)
                    else:
                        tag = TinyTag.get(fr"{track.text}")
                    #print(tag.title, "-", tag.artist)
                    print(tag.title+ "-"+ tag.artist+"\n")
                    writefile.write(tag.title+ " - "+ tag.artist+"\n")
                    numsongs+=1
                except OSError:
                    print("unable to find " + fr"{track.text}")
        print(playlistname+": "+str(numsongs)+" songs")

# exit
input("\n\nPress enter to close.")
