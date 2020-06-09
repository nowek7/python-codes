import re
import os


def run():
    """
    Get compilation time from *.log file.
    """

    # Name current file.
    path = os.path.basename(__file__)
    path = '0000_2klasa.log'

    allTime = 0
    curTime = 0
    book = {}

    try:
        with open(path) as file:
            data = file.readlines()
            i = 0
            for line in data:
                if 'timer' in line:
                    matches = re.findall(r'[0-9]{1,6}', line)
                    if len(matches) == 1:
                        allTime = int(matches[0])
                    else:
                        page = matches[1]
                        book[page] = int(matches[0])
                        curTime += int(matches[0])

                    print(f'All compiling time is {allTime} ms!')
                    print(f'Current compiling time is {curTime} ms!')
    except IOError as error:
        print(f'Was something wrong {os.strerror(error)}')
    except ValueError as error:
        print(f'Was something wrong {os.strerror(error)}')


if __name__ == '__main__':
    run()
