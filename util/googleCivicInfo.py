from urllib import request, parse
from urllib.error import HTTPError # error handling for bad api calls
import json

def getkey(k_file):
    '''retrives api keys based on file name'''
    try:
        f = open(k_file, 'r')
    except FileNotFoundError:
        print("Missing key file, HALP!")
    l = f.read().split('\n')
    f.close()
    return l[0]

googlekey = getkey("util/googleCivic.txt") #gets API key

def civic():
    '''info on a certain politcian'''
    #poke = poke.lower()
    try:
        url = "https://www.googleapis.com/civicinfo/v2/representatives"
        #url = url + poke
        #cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        #stuff = request.urlopen(cri) # GETS STUFF
        #js = stuff.read() # gets info from urlopen
        #jason = json.loads(js)
        #if(poke == ''):
        #    return jason["results"]
        #return jason
    except HTTPError:


    return None
