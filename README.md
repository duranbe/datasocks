![Datasocks](https://github.com/duranbe/datasocks/blob/main/img/logo.png?raw=true)

![Test](https://github.com/duranbe/datasocks/actions/workflows/django.yml/badge.svg)
![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)
![PyPI - Python](https://img.shields.io/badge/python-%3E%3D3.7-blue)
## IoT Made simple 

![Demo](https://github.com/duranbe/datasocks/blob/main/img/demo.PNG?raw=true)
Monitor and remote control in real time your IoT objects without the pain of dealing with Networking.

An account, an API Key and you are good to go !

Datasocks use Websockets Protocol to communicate in an asynchronous way with your IoT devices.

It's for now designed as a self-hosted and private application (or a PoC ? ).

This project was made during and for the [Linode](https://www.linode.com) x [Hashnode](https://hashnode.com/n/linodehackathon) Hackathon 

## How it works

![Schema](https://github.com/duranbe/datasocks/blob/main/img/schema.png?raw=true)

IoT devices are sending data in json format to the Datasocks server, where it can be saved and then redirect to the front-end giving a real-time update on the user web browser.

The user can control the object remotely by creating buttons that will send a special action to the pre-configured device.
## Setup

### Server 
Using Docker

```
git clone https://github.com/duranbe/datasocks.git
docker-compose build
docker-compose --env-file ./.env up
```

### Client
Here is an example of sending data from a device (Python)

```python
import websocket # https://github.com/websocket-client/websocket-client
import json
from random import randint,random
from datetime import datetime

ws = websocket.create_connection(f"ws://<URL>/ws/dashboard/<DASHBOARD_ID>/?api_key=<APIKEY>) 

ws.send(json.dumps(
		{ 	
			"metric_name": "Temp",
			"value": random()*5.65,
			"date": datetime.now().strftime("%d/%m/%Y T %H:%M:%S"),
		}
))
ws.close()
```
## Why not a simple POST/GET system ? 
- Need to setup a web server on the device itself and open the router to the Internet
- No efficient if there is no event (Polling needed)

![Microsoft](https://docs.microsoft.com/fr-fr/azure/application-gateway/media/application-gateway-websocket/websocket.png)
