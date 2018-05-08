#!/usr/bin/python3

import os
import sys

import eyed3
from natsort import natsorted

def change_mp3_tags(
        root_dir: str,
        album: str=None,
        artist: str=None,
        album_artist: str=None,
        genre: str=None
    ) -> None:
    """
    Change the ID3 Tags of the MP3 files and the name. Every informateion which is not set will
    not be used.

    Arguments:
        root_dir {str} -- Path to the root directory.

    Keyword Arguments:
        album {str} -- Name of the Album. (default: {None})
        artist {str} -- Name of the Artist. (default: {None})
        album_artist {str} -- Name of the Album_artist. (default: {None})
        genre {str} -- Name of the Genre. (default: {None})

    Returns:
        None -- [description]
    """
    album_dirs = os.listdir(root_dir)
    if not album_dirs:
        sys.exit()

    sorted_album_dirs = natsorted(album_dirs)

    chapter_counter = 1
    for current_dir in sorted_album_dirs:
        tracks = os.listdir('{0}/{1}'.format(root_dir, current_dir))
        if not tracks:
            sys.exit()

        sorted_tracks = natsorted(tracks)
        for current_track in sorted_tracks:
            file_path = '{0}/{1}/{2}'.format(root_dir, current_dir, current_track)
            audio_file = eyed3.load(file_path)

            print(file_path)
            print('Chapter: {0}'.format(str(chapter_counter)))

            audio_file_title = u'Chapter {:03d}'.format(chapter_counter)
            print('Old - Title: {}'.format(audio_file.tag.title))
            audio_file.tag.title = audio_file_title
            print('New - Title: {}'.format(audio_file.tag.title))

            print('Old - Track Num: {0}'.format(str(audio_file.tag.track_num)))
            audio_file.tag.track_num = chapter_counter
            print('New - Track Num: {0}'.format(str(audio_file.tag.track_num)))

            print('Old - Album: {0}'.format(str(audio_file.tag.album)))
            if album:
                audio_file.tag.album = u'{0} - {1}'.format(album, current_dir)
                print('New - Album: {0}'.format(str(audio_file.tag.album)))

            print('Old - Album Artist: {0}'.format(str(audio_file.tag.album_artist)))
            if album_artist:
                audio_file.tag.album_artist = album_artist
                print('New - Album Artist: {0}'.format(str(audio_file.tag.album_artist)))

            print('Old - Artist: {0}'.format(str(audio_file.tag.artist)))
            if artist:
                audio_file.tag.artist = artist
                print('New - Artist: {0}'.format(str(audio_file.tag.artist)))

            print('Old - Genre: {0}'.format(str(audio_file.tag.genre)))
            if genre:
                audio_file.tag.genre = genre
                print('New - Genre: {0}'.format(str(audio_file.tag.genre)))

            audio_file.tag.save()
            print('Old - File Name: {0}'.format(file_path))
            new_file_path = '{0}/{1}/{2}.mp3'.format(root_dir, current_dir, audio_file_title)
            os.rename(file_path, new_file_path)
            print('New - File Name: {0}'.format(new_file_path))

            chapter_counter += 1

            print('')
