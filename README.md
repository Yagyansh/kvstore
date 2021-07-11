# KV Store

## Overview
Basic KV store web application & CLI Interface written in Python. It has 2 components:
1. The WEB API - This runs via Python flask web server and has 2 functionalites:  
   a. /get - This requires an input of the "key" value for which the value has to be retrieved from the KV store.  
   b. /add - This requires an input of the "key" and "value" that has to be added to the KV store.  
2. CLI Interface - This is a CLI shell that consumes the WEB API and performs actions over the KV store.  
   a. get <key> - Output the values of the provided key from the KV store.  
   b. set <key> <value> - Add the KV pair to the KV store.  
   c. watch - Subscribe to the changes happening to the KV store.  
  
This project contains 2 major python files and 1 pickle data file to introduce data persistance.
1. kvstore.py - This implements the Web API functionality of the project.
2. cli-shell.py - This implements the CLI client created to consume the KV Store Web API.
3. store.pickle - This stores the KV pairs that are added to the KV Store. It is loaded once at the start of the API.

## Requirements
  Python v 3.x  
  Libraries used - flask,cmd,requests,pickle,socket.  

## Installation and Usage
  Download the requirements file and install the required libraries using pip.  
  `$ python3 -m pip install -r requirement.txt`  
  
  Start the Web API  
  `$ python3 kvstore.py`  
  
  Use the CLI Shell  
  `$ python3 cli-shell.py`  
  
## Examples
  
  
