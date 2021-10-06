<p align="center">
<table>
<tr>
<td>
<img align="left" src="https://user-images.githubusercontent.com/77739870/136249792-d424e897-6470-42a0-9904-dd58955ae9b3.png" width="150" height="150">
<h3>Holberton School's: Hack day: Checker challenge</h3>
<ul>
    <li>Command-line checkers for Holberton students.</li>
    <li>Program connests to Holberton's intranet's API.</li>
    <li>It collects student/project data via the command line and runs desired code checker.</li>
</ul>
<img width="1000" height="0">
</td>
</tr>
</table>
</p>

### Requirements:
- Free to build what we want, it just needs to be related to Holberton and the Checker.  
- 24 hour time frame.  

### The Intranet's API
- All endpoints are accessible only with authentication.  
- The authentication on the API is done by requesting an "auth_token" and using it in every request.  
- In my program, the first things users do is enter their intranet log-in information. An "auth_token" is then created that is used in every request.  

### How to use:
```$ git clone https://github.com/cmdelcarmen/hbt_checkers.git```  
```$ cd hbt_checkers```  
```$ ./checkers_main.py```  

*Note*: I **highly** recommend opening up the `checkers_auth_token.py` file and "hard coding" your credentials in. Then opening up the `checkers_main.py` file and either commenting out or removing the statements asking for the user's credentials. That way when you run the program, it only needs the **project ID** and **task number**.

The **project ID** can be found at the end of the project's URL. For example, the URL "https://intranet.hbtn.io/projects/434" for this project indicates **that the project ID** is: 434.

### File descriptions:
- checkers_main.py  
    - File collects the student's login credentials and API key for Holberton's intranet. It also calls all the other functions we are using.
- checkers_get_auth_token.py
    - File contanins method `get_auth_token()` which uses the student's login credentials to return a temporary access token to the intranet's API. 
- checkers_tasks.py
    - File contains method `get_tasks()` which uses the access token and the project ID entered by the user to return a dictionary of all the project's tasks. For example: `{1: task_id}`, 1 is the number of the task, task_id is the is given to the task by Holberton.
- checkers_filename.py
    - File contains method `get_filename()` which uses the access token and task_id (aquired by the user choosing which task number) to return the name of the file that is being checked, so that the student can see the name of the file being checked.
- checkers_correction.py
    - File contains method `get_correction()` which uses the access token and the task_id to run checkers. It lets the user know which checkers passed and which failed, along with the type of checker it was.

### What the program looks like on the terminal:
![image](https://user-images.githubusercontent.com/77739870/136260954-76ff4d93-89ac-4792-9896-0b05a68d33a7.png)
