# usage: given a newline-separated list of words into words.txt, simply run this script to convert them to a json list

import json

words = []
with open("words.txt", "r") as file:
    for line in file:
        word = line.strip()
        words.append(word)

print(json.dumps(words))
