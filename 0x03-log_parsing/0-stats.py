#!/usr/bin/python3


"""
Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the line
    must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), print
    these statistics from the beginning:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear or is not an integer, don’t print
            anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order

Warning: In this sample, you will have random value - it’s normal to not have
the same output as this one.
"""

import sys


def print_stats(size, status):
    """Prints the stats"""

    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key]:
            print("{}: {}".format(key, status[key]))


def main():
    """Main function"""
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
