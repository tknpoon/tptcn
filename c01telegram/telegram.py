#!/usr/bin/python
import smtpd , asyncore, json, os, telepot

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Message addressed from:', mailfrom
        if mailfrom == 'frommail@tknpoon':
            print 'Message addressed to  :', rcpttos
            #print 'Data :',data
            msg = data.splitlines()
            
            #skip to blank line
            while len(msg[0]) > 0:
                del msg[0]
            message = "\n".join(msg)
            print 'Message :', message

            telepot.Bot(os.environ['TELEGRAM_TOKEN']).sendMessage( 
                os.environ['TELEGRAM_CHAT_ID'], message, parse_mode='HTML' 
            )
        return

server = CustomSMTPServer(('0.0.0.0', 25), None)

asyncore.loop()

