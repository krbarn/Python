#!/usr/bin/env python
# Sample program for accessing Livestatus from Python

import json, os, socket

# for local site only: file path to socket
#address = "%s/tmp/run/live" % os.getenv("OMD_ROOT")
# for local/remote sites: TCP address/port for Livestatus socket
address = ("osimon01.unx.sas.com", 6557)

# connect to Livestatus
family = socket.AF_INET if type(address) == tuple else socket.AF_UNIX
sock = socket.socket(family, socket.SOCK_STREAM)
sock.connect(address)

# send our request and let Livestatus know we're done
sock.sendall("GET status\nOutputFormat: json\n")
sock.shutdown(socket.SHUT_WR)

# receive the reply as a JSON string
chunks = []
while len(chunks) == 0 or chunks[-1] != "":
    chunks.append(sock.recv(4096))
sock.close()
reply = "".join(chunks)

# print the parsed reply
print(json.loads(reply))
