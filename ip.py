#!/usr/bin/env python3

from os import environ
from requests import get
from subprocess import call
from time import strftime
from sys import exit

if 'IP_DEST' not in environ.keys():
    exit('Environment variable IP_DEST must be set to `user@host:/path`')

else:       
    ip = get('http://ipinfo.io/ip').text.strip()
    timestamp = strftime('%Y-%m-%d %H:%M:%S')
    
    with open('ip.txt', 'w') as f:
        f.write('{0}\n{1}\n'.format(timestamp, ip))
    
    call('scp ip.txt {}'.format(environ['IP_DEST']), shell=True)
    exit(0)

