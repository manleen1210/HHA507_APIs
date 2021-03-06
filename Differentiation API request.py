# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:18:03 2021

@author: manle
"""
""" 
The following API provides research information on topics relating to physics,
 mathematics, quantitative finance, and economics. In this code I searched for research related 
 to differentiation. I asked to start at index = 0 and find a maximum of 20 results. There are no API keys/secrets 
 or additional authorizations required to connect to this API.
 
"""
import requests

apidocurl = 'https://arxiv.org/help/api/user-manual#Examples'
apiresponse = requests.get(apidocurl)
apiresponse.status_code

mathurl = 'http://export.arxiv.org/api/query?search_query=all:differentiation&start=0&max_results=20'

response = requests.get(mathurl)

response.status_code

responsedata = print(response)

import urllib.request

with urllib.request.urlopen("http://export.arxiv.org/api/query?search_query=all:differentiation&start=0&max_results=20") as mathurl:
    differentiationdata = mathurl.read()
    print(differentiationdata)

repeatmathurl = "http://arxiv.org/api/query?search_query%3Dall%3Adifferentiation%26id_list%3D%26start%3D0%26max_results%3D20"

repeatresponse = requests.get(repeatmathurl)

repeatresponse.status_code

conda install xmltodict

import xmltodict

import json

obj = xmltodict.parse(differentiationdata)

print(json.dumps(obj))

differentiationjson = json.dumps(obj)
diffdata = json.loads(differentiationjson)
import pandas as pd
jsonSimple = pd.DataFrame(diffdata)