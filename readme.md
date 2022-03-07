# My Vulnerable Application
## For BC / IT COMMİTTEE - Cyber Security
Custom vulnerable web application designed to be used during the educational course for NAYORA. 

It is vulnerable to the following attacks:  
* Credentials brute force
* Session Hijacking
* SQL Injection

## Setting Up
1. Set up virtual environment for python
    * Linux
        * sudo pip3 install virtualenv 
        * virtualenv venv
        * source ./venv/bin/activate - to activate virtual environment
        * deactivate - you can use to deactivate venv when it is no longer required
    * Windows
        * pip install virtualenv 
        * virtualenv venv
        * venv\Scripts\activate - to activate virtual environment
        * deactivate - you can use to deactivate venv when it is no longer required
2. Install all required dependencies after the activation of virtual environment
    * pip3 install -r requirements.txt - Linux
    * pip install -r requirements.txt - Windows  
*Reference: https://note.nkmk.me/en/python-pip-install-requirements/* 
3. Set up the database via:
    * python3 init_db.py - if you are using Linux
    * python init_db.py - if you are using Windows
4. Start the server 
    There are 2 servers that you can use to test different vulnerabilities. If you want to test Session Hijacking and Brute Force attack start **server.py**. If you want to test SQL Injection start **server2.py**.  
    To start python Flask server, run following command:  
    * python3 server.py - Windows
    * python server.py - Linux

    The server by default runs on the http://localhost:5000

## Tasks
* Write script that will brute force user credentials - deadline 2 weeks 
* Provide solution for 2 following problems - deadline 1 week:  
    * Fix SQL Injection vulnerability in **server2.py** 
    * In the **server.py** it is possible to login by using following credentials admin:password, even if the password for admin user is different. Find out the its reason and provide solution for that. 
