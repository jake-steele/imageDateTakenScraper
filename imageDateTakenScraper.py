import os
import pandas as pd
import exifread

basepath = '' # Point toward a folder containing only image files and/or folders of only image files
outputFilename = '' + '.xlsx' # Excel spreadsheet filename

entryDictionaries = [] # List to be populated with dictionaries of file details

for (dirName, subdirList, files) in os.walk(basepath):
    for image in files:
        fileProperties = {
            'date': '',
            'filename': image,
            'subdirectory': basepath,
            'extension': ''
        }
        fileProperties['extension'] = os.path.splitext(fileProperties['filename'])[1]
        entryDictionaries.append(fileProperties)

for entry in entryDictionaries:
    filePath = basepath + '/' + entry['filename']
    with open(filePath, 'rb') as imageFile:
        tags = exifread.process_file(imageFile, stop_tag='EXIF DateTimeOriginal')
        dateTaken = tags['EXIF DateTimeOriginal']
        entry['date'] = dateTaken

df = pd.DataFrame(entryDictionaries, columns = ['date', 'filename', 'subdirectory', 'extension'])

# df.to_excel(outputFilename)