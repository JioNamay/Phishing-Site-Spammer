'''This script sends fake email address and password combinations to the specified URL'''

import random
import string
import requests

from credentials import first_names, last_names, passwords

URL = "PHISHING SITE HERE"

def random_email():
    '''Creates and returns a random email address'''

    first = random.choice(first_names).lower()
    last = random.choice(last_names).lower()

    random_bridge_num = random.randint(1, 3)
    random_domain_num = random.randint(1, 3)

    bridge = "." if random_bridge_num == 1 else "_" if random_bridge_num == 2 else ""
    domain = "@gmail.com" if random_domain_num == 1 else "@yahoo.com" if random_domain_num == 2 else "@hotmail.com"
    random_number = ""

    for _ in range(random.randint(0, 4)):
        random_number += random.choice(string.digits)

    return first + bridge + last + random_number + domain

for _ in range(1000): # send 1000 fake logins
    email = random_email()
    password = random.choice(passwords)

    requests.post(URL, allow_redirects=False, data={
        "email": email, # email key may differ from site to site
        "password": password # password key may differ from site to site
    })

    print("Sending email {} and password {}".format(email, password))
