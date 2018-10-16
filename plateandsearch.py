import requests
import json
import sys
from openalpr import Alpr
import time
import numpy as np
import cv2

from collections import namedtuple
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from sinesp_client import SinespClient
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


alpr = Alpr("br", "/usr/local/etc/openalpr/openalpr.conf", "/Users/ornito/Dev/openalpr/runtime_data")
sc = SinespClient()

if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(3)
#alpr.set_default_region("br")

def isArrEmpty(lis1):
    if not lis1:
        return 1
    else:
        return 0

results = alpr.recognize_file("images/placa2.jpg")
alert = 'Nao reconhecido'
data = ''



if isArrEmpty(results):
    print("Nenhuma placa reconhecida")
else:
    plate = results['results'][0]
    for candidate in plate['candidates']:
        recognizedPlate = ''
        recognizedPlate = candidate['plate']
        data = sc.search(str(recognizedPlate))
        if data['return_code'] == '0':
            alert = data['model'] + "-" + data['color'] + "-" + data['model_year'] + "-" + data['status_message']
            break
print (alert)


#print(results.length())
#for plate in results['results']:
#    i += 1
#    print("Plate #%d" % i)
#    print("   %12s %12s" % ("Plate", "Confidence"))
#    for candidate in plate['candidates']:
#        prefix = "-"
#        if candidate['matches_template']:
#            prefix = "*"

#        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

# Call when completely done to release memory
alpr.unload()
