# -*- coding: utf8
# Esse módulo imita o requests

import urllib.request
import ssl

class Get(object): pass

def get(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    g = Get()
    g.status = response.status
    g.text = response.read().decode('utf-8')
    return g