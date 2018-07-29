#!/usr/bin/python
# coding: utf-8


# imports
import sys
from pyzabbix import ZabbixAPI


# cyrillic hack
reload(sys)
sys.setdefaultencoding('utf-8')


# constants
PROBLEM_ACK = 0
PROBLEM_CLOSE = 1
zabbix_api_host = ''
zabbix_user = ''
zabbix_password = ''


# program entry point
if __name__ == '__main__':
    event_ids = ''
    ack_message = ''

    try:
        event_ids = sys.argv[1]
        ack_message = sys.argv[2]
    except IndexError:
        print 'Probably you missed parameters'

    try:
        api = ZabbixAPI(zabbix_api_host)
        api.login(zabbix_user, zabbix_password)

        api.event.acknowledge(eventids=event_ids, message=ack_message, action=PROBLEM_ACK)

    except:
        print 'Zabbix api error'
