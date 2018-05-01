# Readme

## Introduction
This Python script will help you to set ID3 tags for your mp3 audio books on a clean and simple way. The script will iterate over all files which will be in the following structure:  
`root node/CD number/tracks.mp3`

## Requirements
This Python script is written in Python 3.6.3 and it is recommended to have this version installed. It also use the `eyed3` library which you can simply install over pip with `pip install eyed3`. 

## First step
I recommend as first step to execute `audio_book_mp3_tag_changer` with the argument **"-?"** to get a the following list with all allowed arguments.

```
-?      --help          Mandatory:False  Show all valid arguments.
-p      --path          Mandatory:True   Path to the root folder.
-al     --album         Mandatory:False  Name of the album.
-ar     --artist        Mandatory:False  Name of the artist.
-alr    --album-artist  Mandatory:False  Name of the album artist.
-g      --genre         Mandatory:False  Genre of the album.
-i      --interactive   Mandatory:False  Activate the interactive mode.
``` 
