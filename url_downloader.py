import os
import sys
import getopt
import urllib.request

class UrlDownloader:

	def download(self, dest_dir, links):
		if not os.path.exists(dest_directory):
			os.makedirs(dest_directory)

		for link in links:
			last_slash_index = link.rfind("/") 
			last_dot_index = link.rfind(".") 
			if last_slash_index == -1:
				print ("Unable to recognize filename")
				continue
			if last_dot_index == -1 or last_dot_index < last_slash_index:
				print ("Unable to recognize file extension for " + link)
				continue
			downloaded_file_name = link[last_slash_index + 1:]
			urllib.request.urlretrieve(link, "{0}/{1}".format(dest_directory, downloaded_file_name))
			print ("File is saved: " + downloaded_file_name)
			
if __name__ == "__main__":
	config = open("config.txt", "r");
	dest_directory = "downloads"
	links = []
	for line in config:
		links.append(line.rstrip('\n'))

	url_downloader = UrlDownloader()
	url_downloader.download(dest_directory, links)




