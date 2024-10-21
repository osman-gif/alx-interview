#!/usr/bin/env python3


import sys


def print_stats(size, status):
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key]:
            print("{}: {}".format(key, status[key]))


def main():
    size = 0
    status = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) > 2:
                size += int(data[-1])
                if data[-2] in status:
                    status[data[-2]] += 1
            if count == 10:
                print_stats(size, status)
                count = 0
    except KeyboardInterrupt:
        print_stats(size, status)
        raise


if __name__ == "__main__":

    main()

