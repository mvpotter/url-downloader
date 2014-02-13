import os
import urllib

config = open("url-downloader-config.txt", "r");
directory = "downloads"

if not os.path.exists(directory):
    os.makedirs(directory)

i = 0
for line in config:
	urllib.urlretrieve(line, "{0}/{1}.jpg".format(directory, i))
	i += 1

	