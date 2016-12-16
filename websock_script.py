#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import websockets
import sys

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('wss://ezhome-broker.herokuapp.com/submit')

    try:
        token = sys.argv [1]
        device = sys.argv [2]
        state = sys.argv [3]

        try:
            values = sys.argv [4]
            message = str({"token": token, "device": device, "state": state, "values": values}).replace('\'', '\"')
        except:
            scenario = device
            message = str({"token": token, "scenario": scenario, "state": state}).replace('\'', '\"')



        yield from websocket.send(message)
        print("> {}".format(message))

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())
