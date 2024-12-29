#!/usr/local/bin/python3

import selectors
import socket
import sys
sys.path.append('mypymud')
import mudnetwork

mn = mudnetwork.MUDNetwork()

mn.bind()
mn.loop()
