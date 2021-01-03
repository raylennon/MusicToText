
# for getting music metadata
from tinytag import TinyTag

# for navigating file folders, etc.
import glob, os

# for doing quick searches
import re

from bs4 import BeautifulSoup
from html import unescape

playlists = []

# Top-level folder where all playlists and songs are stored
topdir = "C:/Users/lenno/Music/"
os.chdir(topdir)

# saves all playlist files into a list
for path, dirs, files in os.walk(topdir):
    for file in files:
        if file.endswith('.wpl'):
            playlists.append(os.path.join(path, file))

# goes through each playlist and finds files
for playlist in playlists:
    print('\n\n' + playlist[playlist.find('\\')+1:playlist.find('.wpl')]
        + '\n~~~~~~~~~~~~~')
    content = open(playlist, 'r').read()
    quotes = []
    for quote in re.finditer('"', content):
        quotes.append(quote)
    for i in range(len(quotes)-1):
        if content[quotes[i].start()-10:quotes[i].start()] == "media src=":
            track = content[quotes[i].start()+1:quotes[i+1].start()]

            track = BeautifulSoup(unescape(track), 'lxml').text
            tag = TinyTag.get(playlist[0:playlist.find('\\')+1] + track)

            print(tag.title, "-", tag.artist)
    input("\n\nEnter to continue")

# exit
input("\n\nPress enter to close.")
