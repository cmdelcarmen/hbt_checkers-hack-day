#!/usr/bin/python3

import json
import requests


def get_filename(auth_token="", task_id=""):
    """
        Method connects to the intranet's API and gets the github file name
        that is being ran through the code checkers.
    """
    headers = {"Content-Type": "application/json"}
    URL = "https://intranet.hbtn.io/tasks/{}.json?auth_token={}".format(task_id, auth_token)
    response = requests.get(URL, headers=headers)

    #print(json.loads(response.content.decode('utf-8'))['checker_available'])
    return json.loads(response.content.decode('utf-8'))['github_file']
