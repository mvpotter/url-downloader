import os
import sys
import getopt
import argparse
import urllib.request

class UrlDownloader:

	def download(self, dest_dir, links):
		if not os.path.exists(dest_dir):
			os.makedirs(dest_dir)

		for link in links:
			last_slash_index = link.rfind("/") 
			last_dot_index = link.rfind(".") 
			if last_slash_index == -1:
				print ("Unable to recognize filename")
				continue
			if last_dot_index == -1 or last_dot_index < last_slash_index:
				print ("Unable to recognize file extension for {}".format(link))
				continue
			downloaded_file_name = link[last_slash_index + 1:]
			try:
				urllib.request.urlretrieve(link, "{0}/{1}".format(dest_dir, downloaded_file_name))
				print ("File is saved: {}".format(downloaded_file_name))
			except ValueError as e:
				print (e)
			except urllib.error.HTTPError as e:
				print ("{0} for {1}".format(e, link))

			
if __name__ == "__main__":
	DEFAULT_DOWNLOAD_DIR = 'downloads'

	parser = argparse.ArgumentParser(description='Downloads files from the web located by links.')
	parser.add_argument('-l','--links', nargs='*', help='Links of files to be downloaded', metavar='links', required=False)
	parser.add_argument('-c','--config', help='Configuration file with links (each link on a single line)', metavar='config_file', required=False)
	parser.add_argument('-d','--destination', help='Destination directory', default=DEFAULT_DOWNLOAD_DIR, metavar='destination_dir', required=False)
	args = parser.parse_args()
	
	links = []
	if args.links:
		for link in args.links:
			links.append(link)
	if args.config:
		try :
			config = open(args.config, "r");
			for line in config:
				links.append(line.rstrip('\n'))
		except IOError:
			print ("Unable to open file {}".format(args.config))
			exit(1)	
	if len(links) == 0:
		print ("No links to download were provided")
		exit(2)

	url_downloader = UrlDownloader()
	url_downloader.download(args.destination, links)



