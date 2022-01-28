from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pathlib import Path
import argparse
import io
import pyheif
import exifread
import re
import requests
import os
import shutil
import webbrowser
import ipdb

def get_location(latlng):
    p = re.compile(r'formatted_address" : (.+)')

    return re.search(p, r.text).group(1)


def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                print(key, val)
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]
    return geotagging


def latlng_conversion(latlng, ref):
    degrees = latlng[0]
    minutes = latlng[1] / 60.0
    seconds = latlng[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        second = -seconds

    return round(degrees + minutes + seconds, 5)


def get_coordinates(geotags):
    lat = latlng_conversion(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
    lon = latlng_conversion(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat, lon)


def get_exif_data(ifile):
    if re.search(r'jpeg$|jpg$|png$|bmp$', str(ifile), re.IGNORECASE):
        shutil.copy(ifile, destination)
        image = Image.open(ifile) # Load the image file
        exifdata = image._getexif() # Extract the exif data
        if exifdata and exifdata.get(36867) != None:
            return exifdata.get(36867), ifile
        else:
            mkdir_unknown(ifile)
            return 'No exif',  ifile

    elif re.search(r'heic$', str(ifile), re.IGNORECASE):
        shutil.copy(ifile, destination)
        heif_file = pyheif.read_heif(str(ifile)) # Loads the file into the variable
        for metadata in heif_file.metadata: # Search through for a value to get the key
            # ByteasIO is a stream reader to pull in the value instead of opening up the file 
            # First 6 characters in the stream can corrupt our data
            if metadata['type'] == 'Exif':
                fstream = io.BytesIO(metadata['data'][6:])

            tags = exifread.process_file(fstream,details=False) # tags variable is a dictionary
            return str(tags.get("EXIF DateTimeOriginal")), ifile

    elif re.search(r'CR2$|NEF$', str(ifile), re.IGNORECASE):
        shutil.copy(ifile, destination)
        f = open(ifile, 'rb') # 'rb' mode opens the file in binary format for reading

        # Return Exif tags
        tags = exifread.process_file(f,details=False) # detail=False cuts out the bytes commentator 

        return str(tags['EXIF DateTimeOriginal']), ifile


def geo_search(ifile):
        image = Image.open(ifile) # Load the image file
        exifdata = image._getexif() # Extract the exif data
        geotags = get_geotagging(exifdata)
        if geotags:
            lat_long = get_coordinates(geotags)
            geo_loc = get_location(str(lat_long)[1:-1])
            geo_html(exifdata.get(36867), geo_loc, ifile)
        else:
            geo_loc = 'No location Data'
        return exifdata.get(36867), geo_loc, ifile


def make_subdir(img, date):
    os.chdir(destination)
    if date != 'None':
        upd_name = photo_rename(img, date)
        dir_date = date[:4]
        if not os.path.isdir(dir_date):
            os.makedirs(dir_date)
            shutil.move(upd_name, dir_date)
        else:
            shutil.move(upd_name, dir_date)
    else:
        mkdir_unknown(img)


def photo_rename(iname, date):
    os.chdir(destination)
    upd_date = re.sub(r'\D', '-', date[:10]) + '-' + re.sub(r'\D', '', iname)
    renamed = re.sub(r'.+(?=\.)', upd_date, iname)
    os.rename(iname, renamed)
    return renamed


def mkdir_unknown(filename):
    os.chdir(destination)
    if os.path.isdir('unknown'):
        shutil.move(os.path.basename(filename), 'unknown')
    else:
        os.makedirs('unknown')
        shutil.move(os.path.basename(filename), 'unknown')


def geo_html(date, loc, img_p):
    f = open('geolog.html', 'a')
    log = date + ' <b>' + loc + ' </b>' + str(img_p) + '<br />'
    message='<html><head></head><body>' + log + '</body> </html>'
    f.write(message)
    f.close


def remove_org(l):
    result = input('Do you want to remove the photos in the original folder(y/n)? ')
    if result == 'y':
        for i in l:
            os.remove(i)
    elif result == 'n':
        return
    else:
        remove_org(input('Try again (y/n): '))


parser = argparse.ArgumentParser()

parser.add_argument('source', help='Directory with photos to sort')
parser.add_argument('destination', help='Directory with sorted photos')
parser.add_argument('-m', '--maps', help='Generates an HTML file with maps', action='store_true')
parser.add_argument('-x', '--xmove', help='The original photos are deleted after copying', action='store_true')
args = parser.parse_args()

source = os.path.abspath(args.source)
destination = os.path.abspath(args.destination)

if not os.path.isdir(destination):
    os.mkdir(destination)

logfile = open((destination + '/imagelog.txt'), 'a') # all corrupted files will logged here

lst = []

for path in Path(source).rglob('*'): # includes subdirectories and all files
    if path.is_file():
        try:
            date, image_path = get_exif_data(path)
            lst.append(str(image_path))

            if re.match(r'\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}', date):
                make_subdir(os.path.basename(image_path), date)
            else:
                mkdir_unknown(image_path)
        except:
            logfile.write(str(path) + ' is corrupted or not an image file\n')

if args.maps:
    for path in Path(destination).rglob('*'):
        try:
            if path.is_file():
                d, g, i = geo_search(path)
        except:
            continue

if args.maps:
    webbrowser.open_new_tab('geolog.html')

if args.xmove:
    remove_org(lst)

logfile.close()
