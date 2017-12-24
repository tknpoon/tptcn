#!/usr/bin/python
import sys,os,telepot

data = sys.stdin.read()

msg = data.splitlines()

message = "\n".join(msg)
#print 'Message :', message

telepot.Bot(os.environ['TOKEN']).sendMessage( 
    os.environ['CHAT_ID'], message, parse_mode='HTML' 
)
