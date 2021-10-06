#!/usr/bin/python3

import json
import requests
import time


def get_correction(auth_token="", task_id=""):
    """
        Method starts checker correction of task specifided by the user.
    """
    headers = {"Content-Type": "application/json"}
    URL = "https://intranet.hbtn.io/tasks/{}/start_correction.json?auth_token={}".format(task_id, auth_token)
    response = requests.post(URL, headers=headers)
    c_id = response.json()['id']


    # extraxts information from checker once it runs using the correction id
    params = {'auth_token': auth_token}
    time.sleep(10) # allows correction to finish

    response = requests.get('https://intranet.hbtn.io/correction_requests/{}=.json'.format(c_id), headers=headers, params=params)
    checks = json.loads(response.content.decode('utf-8'))['result_display']['checks']

    for check in checks:
        print(check['title'], check['check_label'], end=" ")

        if check['passed']:
            print("passed.")
        else:
            print("failed.")

    print()
