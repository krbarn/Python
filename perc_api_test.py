#!/usr/bin/python
import requests
import getpass

r = requests.get("http://percapi.sas.com/entities/ussadm02",auth=(getpass.getuser(),getpass.getpass(prompt='password: ')))

print r.json() 
