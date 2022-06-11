

import requests
#from sympy import content
import json
import html

import textwrap



def get_feed(p_url):
    r = requests.get(url=p_url)
    jsonparse = json.loads(r.text)
    #jsonparse =  html.escape(jsonparse) 


    #print(jsonparse['votd']['text'])

    return jsonparse['votd']['text']
