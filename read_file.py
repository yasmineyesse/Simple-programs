""" Read file """
# Created by Yenami
# Date : May 24, 2017

with open("file.txt", "r") as myfile:
    text = myfile.read()
print(text)