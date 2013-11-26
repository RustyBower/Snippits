#!/usr/bin/env python

import json
from urllib2 import urlopen

#https://api.bitcoinaverage.com/ticker/USD

def getTicker():
    h = urlopen('https://btc-e.com/api/2/btc_usd/ticker').read()
    return h

def getinfo():
    j = getTicker()
    return json