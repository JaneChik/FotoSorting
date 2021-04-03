import os
import shutil
from datetime import datetime
import filetype

path1 = 'your/path/to/dir'

# function returns [year, month, extension] from path_to_file
def get_date_extension(path_to_file):
    file_date = str(datetime.fromtimestamp(os.stat(path_to_file).st_mtime))
    year = file_date[0:4]
    month = file_date[5:7]
    try:
        file_ext = filetype.guess(path_to_file).extension
    except AttributeError:
        file_ext = 'NotPhoto'

    return [year, month, str(file_ext)]


def check_year_month(path, year, month):
    if not os.path.exists(path + '/' + year):
        os.mkdir(path + '/' + year)
        print(f"Directory for year {year} was created")
    if not os.path.exists(path + '/' + year + '/' + month):
        os.mkdir(path + '/' + year + '/' + month)
        print(f"Directory for month {month} in {year} was created")


for file in os.listdir(path1):
    # generate path to file
    file_path = path1 + '/' + file

    #if it is a directory dont preceed further
    if os.path.isdir(file_path):
        continue

    #get date and extension
    year, month, extension = get_date_extension(file_path)

    #create folders for year and month
    check_year_month(path1, year, month)

    #move file
    if not os.path.exists(path1 + '/' + year + '/' + month + '/' + file):
        shutil.move(file_path, path1 + '/' + year + '/' + month + '/' + file)

