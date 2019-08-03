# setup: pip3 install inflect
# usage: given a newline-separated list of singular words into singulars.txt, simply run this script to pluralize 'em

import inflect
engine = inflect.engine()

with open("singulars.txt", "r") as file:
    for line in file:
        word = line.strip()
        plural = engine.plural(word)
        print(plural)
