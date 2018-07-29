#!/usr/bin/python
# coding: utf-8


# imports
import sys
import json
import requests


# cyrillic hack
reload(sys)
sys.setdefaultencoding('utf-8')


# constants
token = ''
PROBLEM_ACK = 0
PROBLEM_CLOSE = 1
zabbix_api_host = ''
zabbix_api = 'http://{}/api_jsonrpc.php'.format(zabbix_api_host)
zabbix_user = ''
zabbix_password = ''


headers = {
    'content-type': 'application/json'
}

payload_template = {
    'jsonrpc': '2.0',
    'method': '',
    'params': None,
    'auth': None,
    'id': 0
}


# program entry point
if __name__ == '__main__':

    event_ids = ''
    ack_message = ''

    try:
        event_ids = sys.argv[1]
        ack_message = sys.argv[2]
    except IndexError:
        print 'Probably you missed parameters'

    # auth
    payload = payload_template.copy()
    payload['method'] = 'user.login'
    payload['params'] = dict()
    payload['params']['user'] = zabbix_user
    payload['params']['password'] = zabbix_password

    auth = requests.post(url=zabbix_api, data=json.dumps(payload), headers=headers)

    if auth.status_code == 200:
        token = json.loads(auth.content)['result']

    else:
        print 'Zabbix api auth error'

    if len(token) > 0:
        payload = payload_template.copy()
        payload['id'] = 1
        payload['auth'] = token
        payload['method'] = 'event.acknowledge'
        payload['params'] = {}
        payload['params']['eventids'] = event_ids
        payload['params']['message'] = ack_message
        payload['params']['action'] = PROBLEM_ACK

        try:
            ack = requests.post(url=zabbix_api, data=json.dumps(payload), headers=headers)

        except:
            print 'Zabbix api error'
