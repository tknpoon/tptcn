#!/usr/bin/python
import sys,os,telepot

data = sys.stdin.read()

msg = data.splitlines()

message = "\n".join(msg)
#print 'Message :', message

telepot.Bot(os.environ['TELEGRAM_TOKEN']).sendMessage( 
    os.environ['TELEGRAM_CHAT_ID'], message, parse_mode='HTML' 
)
