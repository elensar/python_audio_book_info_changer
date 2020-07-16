# Readme

## Introduction
This Python script will help you to set ID3 tags for your mp3 audio books on a clean and simple way. The script will iterate over all files which will be in the following structure:  
`root node/CD number/tracks.mp3`

## Requirements
This Python script is written in Python 3.6.3 and it is recommended to have this version installed. It also used the [eyed3](https://eyed3.readthedocs.io/en/latest/) library which you can simply install over pip with `pip install eyed3` and the [natsort](https://pypi.org/project/natsort/) library wich you can also install over pip with `pip install natsort`.

## First step
I recommend as first step to execute `audio_book_info_changer.py` with the argument **"-h"** to get a the following list with all allowed arguments.

```
usage: Audio book info changer [-h] [-p PATH] [-al ALBUM] [-ar ARTIST]
                               [-alr ALBUM_ARTIST] [-g GENRE] [-gl] [-i]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the root folder.
  -al ALBUM, --album ALBUM
                        Name of the album.
  -ar ARTIST, --artist ARTIST
                        Name of the artist.
  -alr ALBUM_ARTIST, --album-artist ALBUM_ARTIST
                        Name of the album artist.
  -g GENRE, --genre GENRE
                        Genre of the album.
  -gl, --genre-list     List of all genres.
  -i, --interactive     Activate the interactive mode.
```

## How to run the script
You can run the script entirely with the *arguments* from **First step** or you can run the script in *interactive mode*. It is also possible to mix both modes.

### Interactive mode
The interactive mode is simply the possibility to set the informations over console inputs. If you don't use any arguments on startup, the script will automatically run in *interactive mode*.

On mixing the *argument mode* and *interactive mode* with the *argument* **"-i"** or **"--interactive"** you will only be asked for input for the infos which are not set with *arguments*.
