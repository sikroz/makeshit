#!/usr/bin/env python3
import argparse
from makeshit import MakeShit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, required=True, help="Path to directory where to generate files")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Total count of files")
    parser.add_argument("-s", "--size", type=int, default=100, help="Total size of all files in MB")
    args = parser.parse_args()

    try:
        ms = MakeShit(args.path, args.count, args.size)
        ms.generate_data()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
