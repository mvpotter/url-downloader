url-downloader
==============

Downloads a bunch of files by their URLs.

Console usage
-----

```python
url_downloader.py [-h] [-l [links [links ...]]] [-c config_file] [-d destination_dir]

Downloads files from the web located by links.

optional arguments:
  -h, --help            show this help message and exit
  -l [links [links ...]], --links [links [links ...]]
                        Links of files to be downloaded
  -c config_file, --config config_file
                        Configuration file with links (each link on a single
                        line)
  -d destination_dir, --destination destination_dir
                        Destination directory
```

You can provide a list of URLs to be downloaded right in command line using **-l** key or 
place them in a configuration file (each URL on new line) and provide it using **-c** key.

If destination directory is not set, files will be downloaded to "downloads" folder that is located near the script. 

Module usage
------------
If you use url-downloader as a module, usage is the following:

```python
# Create UrlDownloader object
url_downloader = UrlDownloader()
# Invoke download method
url_downloader.download(destination_directory, list_of_links)
```
