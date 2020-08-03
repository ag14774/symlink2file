"""
Script for converting symlinks to normal files
"""

import argparse
import pathlib


def main():
    """
    Main function
    """
    # pylint: disable=too-many-locals, too-many-statements
    args = argparse.ArgumentParser(description='Convert symlink')

    # Required
    args.add_argument('-p', '--path', type=str, help='path to folder with files')
    args = args.parse_args()

    path = pathlib.Path(args.path)

    for file in path.rglob("*"):
        if file.is_symlink():
            print(file)
            orig_file = file.resolve()
            file.unlink()
            orig_file.link_to(file)


if __name__ == '__main__':
    main()
