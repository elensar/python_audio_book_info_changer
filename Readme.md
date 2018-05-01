# Readme

## Introduction
This Python script will help you to set ID3 tags for your mp3 audio books on a clean and simple way. The script will iterate over all files which will be in the following structure:  
`root node/CD number/tracks.mp3`

## Requirements
This Python script is written in Python 3.6.3 and it is recommended to have this version installed. It also used the [eyed3](https://eyed3.readthedocs.io/en/latest/) library which you can simply install over pip with `pip install eyed3`.

## First step
I recommend as first step to execute `audio_book_info_changer.py` with the argument **"-?"** to get a the following list with all allowed arguments.

```
-?      --help          Mandatory:False  Show all valid arguments.
-p      --path          Mandatory:True   Path to the root folder.
-al     --album         Mandatory:False  Name of the album.
-ar     --artist        Mandatory:False  Name of the artist.
-alr    --album-artist  Mandatory:False  Name of the album artist.
-g      --genre         Mandatory:False  Genre of the album.
-i      --interactive   Mandatory:False  Activate the interactive mode.
```

## How to run the script
You can run the script entirely with the *arguments* from **First step** or you can run the script in *interactive mode*. It is also possible to mix both modes.

### Interactive mode
The interactive mode is simply the possibility to set the informations over console inputs. If you don't use any arguments on startup, the script will automatically run in *interactive mode*.

On mixing the *argument mode* and *interactive mode* with the *argument* **"-i"** or **"--interactive"** you will only be asked for input for the infos which are not set with *arguments*.
