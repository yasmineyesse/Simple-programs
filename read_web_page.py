""" Read a web page : example Google API Translate"""
# Created by Yenami
# Date : May 24, 2017

import urllib.request

key = "YOUR API KEY"
target = "fr"
q = "Hello"
google_api = "https://translation.googleapis.com/language/translate/v2?key="+key+"&target="+target+"&q="+q
page = urllib.request.urlopen(google_api)
