# PythonDevops
---
### Jenkins Setup
First Setup/install the Jenkins Server then access by the port 8080 
```
http://localhost:8080
```
### Install shiningpanda Plugin in Jenkins

The ShiningPanda plugin is a Jenkins plugin that adds Python support to Jenkins
```
Go to Jenkins Dashboard.
Click on "Manage Jenkins" in the left-hand side menu.
Select "Manage Plugins".
Navigate to the "Available" tab and search for "ShiningPanda".
Check the box next to "ShiningPanda" and click on "Install without restart".
```
### Create Freestyle Project
1. Select Source Code Management and Provide Github URL
```
https://github.com/gauravrattan/PythonDevops.git
```
2. In Build Triggers Select GitHub hook trigger for GITScm polling
3. In Build Step Select Python Builder and in Command Section write
```
cd /var/lib/jenkins/workspace/Testing
python test_atg_website.py
```
4. Save the job configuration and click on Build Now.

