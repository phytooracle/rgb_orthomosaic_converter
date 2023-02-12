#!/usr/bin/env python3
"""
Author : eg
Date   : 2022-10-02
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import subprocess as sp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--tiff_file',
                        help='Path to the TIFF file',
                        metavar='str',
                        type=str,
                        required=True)

    parser.add_argument('-r',
                        '--resize',
                        help='Resize value',
                        metavar='int',
                        type=int,
                        default=1000)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    png_file_name = args.tiff_file.replace('.tif', '.png')
    sp.call(f'convert {args.tiff_file} -resize {args.resize}x{args.resize}^ -auto-level -contrast {png_file_name}', shell=True)


# --------------------------------------------------
if __name__ == '__main__':
    main()
