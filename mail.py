#!/usr/bin/python
import smtplib
import os
import re
import time


def smail(txt):
    sender = 'sio260085@126.com'
    user = sender
    password = 's980424'
    sendserver = 'smtp.126.com'

    receiver = '906109475@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect(sendserver)
    smtp.login(user, password)

    mail = f'''From:{sender:s}
        To:{receiver:s}
        Subject:IP ADDRESS
        {txt:s}
        '''.encode('utf-8')
    smtp.sendmail(sender, receiver, mail)
    smtp.close()
    print('called')


while 1:
    nipo = os.popen('ip address').read()
    nip = re.findall('2408:[0-9a-z:]+', nipo)
    bip = ""
    with open('ip', 'r') as ip:
        bip = ip.read().split('\n')
    if (nip[0] == bip[0] or nip[1] == bip[0]) and (nip[0] == bip[1] or nip[1] == bip[1]):
        time.sleep(1800)
        continue
    else:
        with open('ip', 'w') as ip:
            ip.write(nip[0]+'\n'+nip[1])
        mailtxt = nipo+'\nhttp://['+nip[0]+']\nhttp://['+nip[1]+']'
        smail(mailtxt)
        time.sleep(1800)
