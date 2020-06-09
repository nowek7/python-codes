import os
from os.path import basename
import re
import glob

answers = ['y', 'Y', 'YES', 'yes']
path = str(input('Paste a path to directory: '))
answer = str(input('Are you sure?(Y/N)  - '))
if answer in answers:
    book = []
    for file in os.listdir(path):
        if file.endswith('.mobi'):
            book.append(file)

# Delete (year)
for fileName in os.listdir(path):
    if fileName.endswith('.mobi'):
        newFileName = re.sub(r"\s+\(\d{4}\)", '', fileName)
        # fileName = basename(fileName)
        # newFileName = basename(newFileName)
        os.rename(fileName, newFileName)
