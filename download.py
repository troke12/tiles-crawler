# download the images from https://3.basemaps.cartocdn.com/dark_all/{i}/{j}/{k}.png
# make sure to change the url or change the theme
import urllib.request
import os

def download_image(url, file_name):
    try:
        urllib.request.urlretrieve(url, file_name)
    except:
        print('retrying...')
        download_image(url, file_name)

def make_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def main():
    for i in range(0, 11):
        for j in range(0, 2**i):
            folder_name = 'images/' + str(i) + '/' + str(j)
            make_folder(folder_name)
            for k in range(0, 2**i):
                url = 'https://3.basemaps.cartocdn.com/dark_all/' + str(i) + '/' + str(j) + '/' + str(k) + '.png'
                file_name = folder_name + '/' + str(k) + '.png'
                if not os.path.exists(file_name):
                    print('downloading ' + file_name)
                    download_image(url, file_name)
                else:
                    print(file_name + ' exists')

if __name__ == '__main__':
    main()
