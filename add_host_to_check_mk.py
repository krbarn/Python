#!/usr/bin/python

import json
import mechanize

check_mk_host="http://myhost.test.com"

check_mk_username="autouser"

check_mk_password="XXXXXXXXXX"

url="/inttest/check_mk/webapi.py"

request_url = "%s%s?action=add_host&_username=%s&_secret=%s" % ( check_mk_host, url, check_mk_username, check_mk_password )

request_data = {}

request_data['attributes'] = {}

request_data['attributes']['tag_agent'] = 'cmk-agent'

request_data['hostname'] = "dbsmyt33.unx.sas.com"

request_data['folder'] = "os/linux"

request_data = json.dumps(request_data)

data = "request=%s" % request_data

br = mechanize.Browser()

br.open(mechanize.Request(request_url, data=data))
