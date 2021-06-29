import os
import re

if __name__ == '__main__':
    path = ''
    # TODO Check path


    book = []
    for file in os.listdir(path):
        if file.endswith('.mobi'):
            book.append(file)

    # Delete (year)
    for fileName in os.listdir(path):
        if fileName.endswith('.mobi'):
            newFileName = re.sub(r"\s+\(\d{4}\)", '', fileName)
            # fileName = os.path.basename(fileName)
            # newFileName = os.path.basename(newFileName)
            os.rename(fileName, newFileName)
