import sys
import urllib.parse
import requests


VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'

VERIFY_URL = VERIFY_URL_PROD

print ('content-type: text/plain')
print ()


#param_str = 'mc_gross=0.02&protection_eligibility=Ineligible&address_status=confirmed&payer_id=AT4UKNZCXBV8Q&address_street=1038 Franklee Lane&payment_date=13:13:48 Apr 28, 2018 PDT&payment_status=Completed&charset=windows-1252&address_zip=19403&first_name=amir&mc_fee=0.02&address_country_code=US&address_name=amir mubarak&notify_version=3.9&custom=&payer_status=verified&business=east.controller@gmail.com&address_country=United States&address_city=Eagleville&quantity=1&verify_sign=AmpgsTjqcPWA1uGoP0eq5p4CKCz9AugCwxQJWFtJD8rrOpVO7xUL6ZAr&payer_email=mubarak117136@gmail.com&txn_id=2E9067579R399060J&payment_type=instant&last_name=mubarak&address_state=PA&receiver_email=east.controller@gmail.com&payment_fee=0.02&shipping_discount=0.00&insurance_amount=0.00&receiver_id=FM9PWNNTWV4FS&txn_type=express_checkout&item_name=&discount=0.00&mc_currency=USD&item_number=&residence_country=US&shipping_method=Default&transaction_subject=&payment_gross=0.02&ipn_track_id=75016d385f4ac'
#params = urllib.parse.parse_qsl(param_str)
params = "[('cmd', '_notify-validate'), ('mc_gross', '0.02'), ('protection_eligibility', 'Ineligible'), ('address_status', 'confirmed'), ('payer_id', 'AT4UKNZCXBV8Q'), ('address_street', '1038 Franklee Lane'), ('payment_date', '13:46:44 Apr 28, 2018 PDT'), ('payment_status', 'Completed'), ('charset', 'windows-1252'), ('address_zip', '19403'), ('first_name', 'amir'), ('mc_fee', '0.02'), ('address_country_code', 'US'), ('address_name', 'amir mubarak'), ('notify_version', '3.9'), ('payer_status', 'verified'), ('business', 'east.controller@gmail.com'), ('address_country', 'United States'), ('address_city', 'Eagleville'), ('quantity', '1'), ('verify_sign', 'AyGUvrznueKCGP.cPDP3LjCvZXEWA1F.08t47KnIm9mRuId2Dz-oXYMI'), ('payer_email', 'mubarak117136@gmail.com'), ('txn_id', '8Y914156P0390964E'), ('payment_type', 'instant'), ('last_name', 'mubarak'), ('address_state', 'PA'), ('receiver_email', 'east.controller@gmail.com'), ('payment_fee', '0.02'), ('shipping_discount', '0.00'), ('insurance_amount', '0.00'), ('receiver_id', 'FM9PWNNTWV4FS'), ('txn_type', 'express_checkout'), ('discount', '0.00'), ('mc_currency', 'USD'), ('residence_country', 'US'), ('shipping_method', 'Default'), ('payment_gross', '0.02'), ('ipn_track_id', 'dc7cbf969795')]"


#params.append(('cmd', '_notify-validate'))


headers = {'content-type': 'application/x-www-form-urlencoded',
           'user-agent': 'Python-IPN-Verification-Script'}
r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
r.raise_for_status()

if r.text == 'VERIFIED':
    print('y')
elif r.text == 'INVALID':
    print('n')
