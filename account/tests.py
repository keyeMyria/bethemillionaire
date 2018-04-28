import sys
import urllib.parse
import requests


VERIFY_URL_PROD = 'https://www.bethemillionaire.com/account/paypal-ipn/'


VERIFY_URL = VERIFY_URL_PROD

# Read and parse query string
param_str = 'mc_gross=0.02&protection_eligibility=Ineligible&address_status=confirmed&payer_id=AT4UKNZCXBV8Q&address_street=1038 Franklee Lane&payment_date=06:20:33 Apr 28, 2018 PDT&payment_status=Completed&charset=windows-1252&address_zip=19403&first_name=amir&mc_fee=0.02&address_country_code=US&address_name=amir mubarak&notify_version=3.9&custom=&payer_status=verified&business=east.controller@gmail.com&address_country=United States&address_city=Eagleville&quantity=1&verify_sign=AI3n-jk4PUusLiPoGGCSCVTnLGRWAC87TwnSTBz-PsmhQe50hTx1Hd6L&payer_email=mubarak117136@gmail.com&txn_id=6JD83390XM514012G&payment_type=instant&last_name=mubarak&address_state=PA&receiver_email=east.controller@gmail.com&payment_fee=0.02&shipping_discount=0.00&insurance_amount=0.00&receiver_id=FM9PWNNTWV4FS&txn_type=express_checkout&item_name=&discount=0.00&mc_currency=USD&item_number=&residence_country=US&shipping_method=Default&transaction_subject=&payment_gross=0.02&ipn_track_id=e822d32a60b26'
params = urllib.parse.parse_qsl(param_str)



# Add '_notify-validate' parameter
#params.append(('cmd', '_notify-validate'))

headers = {'content-type': 'application/x-www-form-urlencoded',
           'user-agent': 'Python-IPN-Verification-Script'}
r = requests.post(VERIFY_URL, data=params, headers=headers, verify=True)
r.raise_for_status()

print(r)

"""
if r.text == 'VERIFIED':
    print('y')
elif r.text == 'INVALID':
    print('n')
"""

