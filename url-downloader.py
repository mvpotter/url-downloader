import os
import urllib.request

config = open("url-downloader-config.txt", "r");
dest_directory = "downloads"

if not os.path.exists(dest_directory):
    os.makedirs(dest_directory)

for line in config:
	line = line.rstrip('\n')
	last_slash_index = line.rfind("/") 
	last_dot_index = line.rfind(".") 
	if last_slash_index == -1:
		print ("Unable to recognize filename")
		continue
	if last_dot_index == -1 or last_dot_index < last_slash_index:
		print ("Unable to recognize file extension for " + line)
		continue
	downloaded_file_name = line[last_slash_index + 1:]
	urllib.request.urlretrieve(line, "{0}/{1}".format(dest_directory, downloaded_file_name))
	print ("File is saved: " + downloaded_file_name)
	