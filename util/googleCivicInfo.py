from urllib import request, parse
from urllib.error import HTTPError # error handling for bad api calls
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def getkey(k_file):
    '''retrives api keys based on file name'''
    try:
        f = open(k_file, 'r')
        l = f.read().split('\n')
        f.close()
        return l[0]
    except FileNotFoundError:
        print("Missing key file, HALP!")
        return None

googlekey = getkey("util/googleCivic.txt") #gets API key

def civic(zip_code):
    '''info on all politician in a zip_code'''
    try:
        url = "https://www.googleapis.com/civicinfo/v2/representatives?key=" + googlekey
        url += "&address=" + str(zip_code)
        cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        stuff = request.urlopen(url) # GETS STUFF

        js = stuff.read() # gets info from urlopen
        jason = json.loads(js)
        jason["officials"].reverse()
        return jason["officials"]
    except HTTPError:
        return "error"
    return None

