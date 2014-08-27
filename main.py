#!/usr/bin/env python3

import argparse
from makeshit import MakeShit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="Path to directory for make files")
    parser.add_argument("-f", "--files", type=int, help="Total count files")
    parser.add_argument("-s", "--size", type=int, help="Total size all files in MB")
    args = parser.parse_args()

    try:
        ms = MakeShit(args.path, args.files, args.size)
        ms.generate_data()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()