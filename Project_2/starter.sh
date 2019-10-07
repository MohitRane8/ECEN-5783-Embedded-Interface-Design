#!/bin/bash

tor="python3 server.py"
node="python3 prototype_1.py"
gui="node websocket-server.js"

konsole -e $tor & konsole -e $node & konsole -e $gui
