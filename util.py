"""
This is a set of utility scripts I will use to work with aspects of my AWS stuff
"""

import json

def loadCred(credfile):
# Loads credentials expects a file in the following format
# { "access":"awd access key", "secret":"aws secret key"
    with open(credfile, 'r') as fptr:
        data = json.load(fptr)
    return data


def run():
    print "Nothing Defined"


if __name__ == "__main__":
    run()