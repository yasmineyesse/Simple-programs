""" Read jsonlines file """
# Created by Yenami
# Date : May 31, 2017

import jsonlines

with jsonlines.open("example_jsonl.jsonl") as reader:
    for obj in reader:
        print(obj)

"""
example.jsonl :
{'a': '1'}
{'b': '2'}
"""