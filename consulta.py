import requests
import json
import sys

from collections import namedtuple
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from sinesp_client import SinespClient
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


sc = SinespClient()

if sys.argv[0]:
  data = sc.search(sys.argv[1])
else:
  data = ''

result = json.dumps(data, indent=4, sort_keys=True).decode('unicode-escape')

print (result)
