#!/usr/bin/python3

import json
import requests
from flask import Flask


def get_tasks(auth_token="", project_id=""):
    """
        Method connects to the intranet's API and returns a dictionary of every task
        along with its id. For example: {"Task 1": task_id}
    """
    headers = {"Content-Type": "application/json"}
    URL = "https://intranet.hbtn.io/projects/{}.json?auth_token={}".format(project_id, auth_token)
    tasks = requests.get(URL, headers=headers).json()['tasks']

    count = 0
    tasks_dict = {}

    for task in tasks:
        tasks_dict[count] = task['id']
        count = count + 1

    return tasks_dict
