# -*- coding:utf-8 -*-
import requests
import re
import smtplib
from email.mime.text import MIMEText

def send_mail(content, to_list=["xxx@gmail.com", "xxx@gmail.com"]):
    username = "xxx"
    password = "xxx"
    me = "xxx@gmail.com"
    msg = MIMEText(content, 'plain')
    msg['Subject'] = 'UTAustin Informal Badminton Schedule'
    msg['From'] = "Notification"
    msg['To'] = "xxx@gmail.com, xxx@gmail.com"
    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)
        smtp.sendmail(me, to_list, msg.as_string())
        smtp.close()
    except Exception:
        print('send email error')

def ut_badminton_schedule():
    url = 'https://www.utrecsports.org/facilities/facility-schedules'
    html = requests.get(url).text
    html = re.sub('\s+', '', html)

    regx = '<aname="\d{6}"></a>(.{1,30})</td>|<td>(.{0,20})</td><td>(.{5,15})</td><td>InformalBadminton'
    p = re.compile(regx)
    items = re.findall(p, html)

    location_map = {'Room348':'BEL', 'Room2.200(ct.3)':'RSC'}

    content = ''
    for i in range(len(items)):
        if items[i][0] != '':
            current_day = items[i][0].split(',')
        else:
            content += f'{current_day[0]}  {current_day[1]}  {location_map[items[i][1]]}  {items[i][1]}  {items[i][2]}\n'
            if current_day[0] == 'Sunday':
                content += '\n'
    send_mail(content)

if __name__ == '__main__':
    ut_badminton_schedule()
