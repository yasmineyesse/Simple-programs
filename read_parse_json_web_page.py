""" Parse JSON from web page """
# Created by Yenami
# Date : May 24, 2017
from read_web_page import *
import json

# parse the json
datas = json.loads(strpage) #loads : charger une chaine de car au format JSON
print(datas)

# return the translated text
for i in datas["data"]["translations"]:
    translatedText = datas["data"]["translations"][0]["translatedText"]
    print(translatedText)