# ccwc.py
#
# Coding Challenges - Build Your Own wc Tool

# Step One: Write a program that accepts the command line option "-c" and a file
# and outputs the number of bytes in the file.

import os
import argparse
import sys


def count_bytes(text: str):
    return len(text.encode(encoding="utf-8", errors="strict"))


def count_file_bytes(file: str):
    statinfo = os.stat(file)
    return statinfo.st_size


def count_file_lines(file: str):
    with open(file, "rt") as f:
        return len(f.readlines())


def count_file_words(file: str):
    with open(file, "rt") as f:
        contents = f.read()
    return len(contents.split())


def init_parser():
    parser = argparse.ArgumentParser(description="wc tool written in Python")
    parser.add_argument(
        "-c",
        help="The number of bytes in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-l",
        help="The number of lines in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-w",
        help="The number of words in each input file is written to the standard output.",
    )
    return parser


if __name__ == "__main__":
    parser = init_parser()
    namespace = parser.parse_args(sys.argv[1:])

    print(f"\t{count_file_words(namespace.w)} {namespace.w}")
    # print(f"\t{count_file_lines(namespace.l)} {namespace.l}")
    # print(f"\t{count_file_bytes(namespace.c)} {namespace.c}")
