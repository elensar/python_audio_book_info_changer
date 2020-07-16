# -*- encoding: utf-8 -*-
# !/usr/bin/python3.7

import argparse
import sys

from eyed3 import id3

import mp3_info_changer
from helper import utils

parser = argparse.ArgumentParser(allow_abbrev=False, prog='Audio book info changer')
parser.add_argument(
    '-p',
    '--path',
    help='Path to the root folder.',
    type=str,
    default='.'
)
parser.add_argument(
    '-al',
    '--album',
    type=str,
    help='Name of the album.'
)
parser.add_argument(
    '-ar',
    '--artist',
    type=str,
    help='Name of the artist.'
)
parser.add_argument(
    '-alr',
    '--album-artist',
    type=str,
    help='Name of the album artist.'
)
parser.add_argument(
    '-g',
    '--genre',
    type=str,
    help='Genre of the album.'
)
parser.add_argument(
    '-gl',
    '--genre-list',
    help='List of all genres.',
    action="store_true"
)
parser.add_argument(
    '-i',
    '--interactive',
    help='Activate the interactive mode.',
    action="store_true"
)

args = parser.parse_args()

if args.genre_list:
    genrelist = id3.genres.items()
    for genre in genrelist:
        genre_number = genre[0]
        genre_name = genre[1]

        if isinstance(genre_number, int) \
            and genre_name is not None \
            and isinstance(genre_name, str):
            print('{0:3d}: {1}'.format(genre[0], genre[1]))

    if not args.interactive:
        sys.exit()

if not args.path:
    raise ValueError('Path must not be empty!')

mp3_info_changer.change_mp3_tags(
    args.path,
    args.album,
    args.artist,
    args.album_artist,
    args.genre
)
