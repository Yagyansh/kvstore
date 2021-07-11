#!/usr/bin/env python3

import cmd
#from kvstore import subscribe
import requests

called = False

class KVShell(cmd.Cmd):
    intro = "CLI Client to consume the KV Web API. Type help or ? to list commands."
    prompt = '(kv-cli)'
    
    def do_get(self, key):
        """Get the value of the provided key.
Syntax - get <key>"""
        if len(key.split()) == 1:
            params = {'key': key}
            api_url = 'http://127.0.0.1:5000/get'
            response = requests.get(api_url,params=params)
            print(response.content)
        else:
            print("Error: Incorret Input! Please follow the syntax - get <key>")
    
    def do_set(self,input):
        """Set the value of the provided key.
Syntax - set <key> <value>"""
        global called
        if len(input.split()) == 2:
            key,value = [str(s) for s in input.split()]
            params = {'key': key, 'value': value}
            api_url = 'http://127.0.0.1:5000/add'
            response = requests.post(api_url,params=params)
            print(response.content)
            called = True
        else:
            print("Error: Incorret Input! Please follow the syntax - set <key> <value>")
    
#    def do_watch(self):
#        global called
#        while True:

    def do_quit(self, line):
        """To exit the shell."""
        return True

if __name__ == '__main__':
    KVShell().cmdloop()