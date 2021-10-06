#!/usr/bin/python3

import json
import sys
import requests


def get_auth_token(api_key="", email="", password=""):
    """
        Method returns the students authorization token for the intranet's API
    """
    URL = "https://intranet.hbtn.io/users/auth_token.json"
    headers = {"Content-Type": "application/json"}

    student_data = '{{\
       "api_key": "{}",\
       "email": "{}",\
       "password": "{}",\
       "scope": "checker"}}'.format(api_key, email, password)

    response = requests.post(URL, headers=headers, data=student_data)

    if response.status_code == 401:
        print("The wrong API key was entered.")
        sys.exit()

    auth_token = json.loads(response.content.decode('utf-8'))['auth_token']

    return auth_token
