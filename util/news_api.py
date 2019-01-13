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

newskey = getkey("util/newsApi.txt") #gets API key
nytimeskey = getkey("util/nytApi.txt")

def news_api(query):
    '''news articles from News API after given a query'''
    # try:
    url = "https://newsapi.org/v2/everything?&apiKey=" + newskey
    url += "&q=" + query
    # url += 'domains=nytimes.com'
    cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    stuff = request.urlopen(url) # GETS STUFF

    js = stuff.read() # gets info from urlopen
    jason = json.loads(js)
    return jason["articles"]
    # except HTTPError:
    #     return "error"
    return None

def nyt_news(query):
    '''news articles from NY Times after given a query'''
    try:
        url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=" + nytimeskey
        url += "&q=" + query.replace(" ", "+")
        # url += 'facet_field=day_of_week'
        cri = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        stuff = request.urlopen(url) # GETS STUFF

        js = stuff.read() # gets info from urlopen
        jason = json.loads(js)
        return jason["response"]["docs"]
    except HTTPError:
        return "error"
    return None
