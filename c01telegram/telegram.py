#!/usr/bin/python
import smtpd , asyncore, json, os, telepot

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        token = os.environ['TOKEN']
        chat_id = os.environ['CHAT_ID']
        print 'Message addressed from:', mailfrom
        if mailfrom == 'frommail@tknpoon':
            print 'Message addressed to  :', rcpttos
            #print 'Data :',data
            msg = data.splitlines()
            #skip to blankline
            while len(msg[0]) > 0:
                del msg[0]
            #del msg[0]
            
            message = "\n".join(msg)
            print 'Message :', message
            TelegramBot = telepot.Bot(token)
            TelegramBot.sendMessage(chat_id, message, parse_mode='HTML')
        return

server = CustomSMTPServer(('0.0.0.0', 25), None)
asyncore.loop()
