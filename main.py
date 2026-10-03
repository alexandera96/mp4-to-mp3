"""MP4 to MP3 — Extract the audio track from an MP4 and write an MP3 at a bitrate you set."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='mp4_to_mp3',
        description='Extract the audio track from an MP4 and write an MP3 at a bitrate you set.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('MP4 to MP3')
    print('Talking-head video into an audio file.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
