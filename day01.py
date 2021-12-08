import zipfile as zip
import os

curr_file = ""
# unziped is the name of the file in the current directory containing the zip file
# unzip the file 2021 times as it was stated in the exercise
for i in range(0, 2021):
    curr_file = os.listdir('unziped')[0]
    with zip.ZipFile('unziped/' + curr_file, 'r') as source:
        source.extractall('unziped')

    os.remove('unziped/' + curr_file)
