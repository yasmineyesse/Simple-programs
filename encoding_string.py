""" Encoding string """
# Created by Yenami
# Date : May 24, 2017
import urllib.request

sentence = "How is"
# encode query to pass to url
sentence_encoded = urllib.parse.quote(sentence)
print(sentence_encoded)

# sentence_encoded can pass on URL