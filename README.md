# Script for acknoledge triggers in dashboard via zabbix api
 
Quite simple script, that awaits two positional arguments at startup:

1. event_ids - event id we want to acknoledge
2. message - acknoledge message

# Modifications

1. zbx_event_ack.py - first simple version, based on `pyzabbix` API wrapper.
2. zbx_pure_event_ack.py - pure 2.7 requests based vesion.

For using first version, just install `pyzabbix` package:

```bash
pip install pyzabbix
```
