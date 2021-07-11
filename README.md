# KV Store

## Overview
Basic KV store web application & CLI Interface written in Python. It has 2 components:
1. The WEB Server - This runs via Python flask web server and has 2 functionalites:  
   a. `/get` - This requires an input of the "key" value for which the value has to be retrieved from the KV store.  
   b. `/add` - This requires an input of the "key" and "value" that has to be added to the KV store.  
   c. `/get_all` - This displays all the available KV pairs in the store.  
2. CLI Interface - This is a CLI shell that consumes the WEB API and performs actions over the KV store.  
   a. `get <key>` - Output the values of the provided key from the KV store.  
   b. `put <key> <value>` - Add the KV pair to the KV store.  
   c. `watch` - Subscribe to the changes happening to the KV store.  
   d. `getall` - This displays all the available KV pairs in the store.  
  
This project contains 2 python files and 1 pickle data file to handle data persistance.
1. kvstore.py - This implements the Web API functionality of the project.
2. kv-cli.py - This implements the CLI client created to consume the KV Store Web Server.
3. store.pickle - This stores the KV pairs that are added to the KV Store. It is loaded once at the start of the API.

## Requirements
  Python 3.8.x and above.   
  Libraries used - flask,cmd,requests,pickle,socket,gevent.  

## Installation and Usage
  Download the requirements file and install the required libraries using pip.  
  `$ python3.8 -m pip install -r requirement.txt`  
  
  Start the Web Server (Default Port - 5000)  
  `$ python3.8 kvstore.py`  
  To run the Web Server in background in Linux - `$ nohup python3.8 kvstore.py &`  
  
  Use the CLI Shell  
  `$ python3.8 kv-cli.py`  
  
## Examples
  1. `$ python3.8 kv-cli.py`  
      CLI Client to consume the KV Web API. Type help or ? to list commands. To exit press 'Ctrl + D' or fire 'quit' command.  
      ```
      kvstore> put test 1  
      b'Successfully added Value - 1 for Key - test'  
      kvstore> get test  
      b'1'
      kvstore>  
      ```
      
  2. Invoke 2 simultaneous CLI shells - one for watch and another to make changes to KV.  
   `$ python3.8 kv-cli.py`  
      CLI Client to consume the KV Web API. Type help or ? to list commands. To exit press 'Ctrl + D' or fire 'quit' command.  
      ```
      kvstore> watch  
      b'Successfully added Value - 1 for Key - test'  
      b'Successfully added Value - 2 for Key - test1'  
      ^C  
      Got keyboard interrupt, exiting!!  
      kvstore>  
      ```
     `$ python3.8 kv-cli.py`  
        CLI Client to consume the KV Web API. Type help or ? to list commands. To exit press 'Ctrl + D' or fire 'quit' command.  
        ```
        kvstore> put test 1    
        b'Successfully added Value - 1 for Key - test'  
        kvstore> put test1 2  
        b'Successfully added Value - 2 for Key - test1'  
        kvstore>  
        ```      
  3. Help to see all the commands.  
       `$ python3.8 kv-cli.py`  
        CLI Client to consume the KV Web API. Type help or ? to list commands. To exit press 'Ctrl + D' or fire 'quit' command.  
        ```
        kvstore> help  

         Documented commands (type help <topic>):
         ========================================
         EOF  get  help  quit  put  watch getall  
        kvstore>  
        ```
