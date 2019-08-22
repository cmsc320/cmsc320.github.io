#!/usr/bin/env python

""" crawler.py: CMSC320 Fall 2019 website PDF/PPTX crawler """

import re
import requests
from bs4 import BeautifulSoup
from os import path
try:
    import urllib
except ImportError:
    from urlparse import urlparse

__author__ = "John P. Dickerson"
__license__ = "GPL"

def main(url, outbase):
    
    # HTTP GET request sent to the URL url
    r = requests.get( url )

    # Use BeautifulSoup to parse the GET response
    root = BeautifulSoup( r.content )
    lnks = root.find("div", id="schedule")\
               .find("table")\
               .find("tbody").findAll("a")

    # Cycle through the actual href for each anchor, checking
    # to see if it's a PDF/PPTX link or not
    for lnk in lnks:
        href = lnk['href']
        # If it's a PDF/PPTX link, queue a download
        if href.lower().endswith(('.pdf', '.pptx')):
            urld = urllib.parse.urljoin(url, href)
            rd = requests.get(urld, stream=True)
            
            # Write the downloaded PDF to a file at ./<name-of-href-PDF>
            outfile = path.join(outbase, href)
            with open(outfile, 'wb') as f:
                f.write(rd.content)
            print("Wrote file to {0}".format(outfile))


if __name__ == '__main__':
    url = "https://cmsc320.github.io/"
    outbase = "./"
    main(url, outbase)
