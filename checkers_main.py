#!/usr/bin/python3
"""
    Written by Caroline Del Carmen for Holberton School's: Hack day: Checker challenge!

    The program collects user input from the command line regarding which project and
    specific question they want to run the code checkers for. Using the Holberton School's
    intrant API, the code checkers are ran on their code. After the checks are ran, the user
    gets notified of how many they passed and how many they failed.

"""

get_auth_token = __import__('checkers_auth_token').get_auth_token
get_tasks = __import__('checkers_tasks').get_tasks
get_filename = __import__('checkers_filename').get_filename
get_correction = __import__('checkers_correction').get_correction

import sys

print("Welcome to the command line checkers!")
print("_____________________________________\n")
print("Your project number can be found at the end of the project URL.")
print("For exmaple, for URL https://intranet.hbtn.io/projects/434, the project number will be 434.")
print("Please make sure to push all you code to github before running the checkers.")
print("Your API key can be found at: https://intranet.hbtn.io/dashboards/my_tools.\n")


# users feel free to remove this section and set your information
# in the checkers_auth_token.py file to avoid repetition
api_key = input("Please enter your API key: ")
email = input("Please enter your email: ")
password = input("Please enter your password for the intranet: ")

auth_token = get_auth_token(api_key, email, password)

project_id = input("Enter project id: ")
print()
tasks_dictionary = get_tasks(auth_token, project_id)

while (1):
    task_number = input("Please enter the task number or exit: ")
    if task_number == "exit":
        sys.exit()

    task_id = tasks_dictionary[int(task_number)]

    github_filename = get_filename(auth_token, task_id)
    print("Running code checkers for file {}: ..... \U0001f600".format(github_filename))

    get_correction(auth_token, task_id)
