import sys
import urllib.parse
import requests


VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'


VERIFY_URL = VERIFY_URL_PROD

# Read and parse query string
param_str = sys.stdin.readline().strip()
params = urllib.parse.parse_qsl(param_str)

# Add '_notify-validate' parameter
params.append(('cmd', '_notify-validate'))

headers = {'content-type': 'application/x-www-form-urlencoded',
           'user-agent': 'Python-IPN-Verification-Script'}
r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
r.raise_for_status()


if r.text == 'VERIFIED':
    print('y')
elif r.text == 'INVALID':
    print('n')
