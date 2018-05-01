#!/usr/bin/python3

import sys

from converter import argument_converter
from converter.argument import argument
from helper import utils
import mp3_info_changer

help_arg = argument('-?', '--help', False, 'Show all valid arguments.')
path_arg = argument('-p', '--path', True, 'Path to the root folder.')
album_arg = argument('-al', '--album', False, 'Name of the album.')
artist_arg = argument('-ar', '--artist', False, 'Name of the artist.')
album_artist_arg = argument('-alr', '--album-artist', False, 'Name of the album artist.')
genre_arg = argument('-g', '--genre', False, 'Genre of the album.')
interactive_arg = argument('-i', '--interactive', False, 'Activate the interactive mode.')

valid_args = [
    help_arg,
    path_arg,
    album_arg,
    artist_arg,
    album_artist_arg,
    genre_arg,
    interactive_arg
]

argument_help_text = argument_converter.valid_argument_text(valid_args)

print(sys.argv)

help_argument = argument_converter.get_argument(sys.argv, help_arg)
if help_argument:
    print(argument_help_text)
    sys.exit()

interactive_argument = argument_converter.get_argument(sys.argv, interactive_arg)
path_value = argument_converter.get_clean_argument_value(sys.argv, path_arg)
album_value = argument_converter.get_clean_argument_value(sys.argv, album_arg)
artist_value = argument_converter.get_clean_argument_value(sys.argv, artist_arg)
album_artist_value = argument_converter.get_clean_argument_value(sys.argv, album_artist_arg)
genre_value = argument_converter.get_clean_argument_value(sys.argv, genre_arg)

if interactive_argument:
    if not path_value:
        path_value = utils.get_input_value('Path', True)

    if not album_value:
        album_value = utils.get_input_value('Album')

    if not artist_value:
        artist_value = utils.get_input_value('Artist')

    if not album_artist_value:
        album_artist_value = utils.get_input_value('Album Artist')

    if not genre_value:
        genre_value = utils.get_input_value('Genre')

if not path_value:
    raise ValueError('Path must not be empty!')

mp3_info_changer.change_mp3_tags(
    path_value,
    album_value,
    artist_value,
    album_artist_value,
    genre_value
)
