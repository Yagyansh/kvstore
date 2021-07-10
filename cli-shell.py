#!/usr/bin/env python3

import cmd
import requests

class KVShell(cmd.Cmd):
    """Simple command processor example."""
    
    def do_get(self, key):
        """Get the value of the provided key.
Syntax - get <key>"""
        params = {'key': key}
        api_url = 'http://127.0.0.1:5000/get'
        response = requests.get(api_url,params=params)
        print(response.content)
    
    def do_set(self,input):
        """Set the value of the provided key.
Syntax - set <key> <value>"""
        key,value = [str(s) for s in input.split()]
        params = {'key': key, 'value': value}
        api_url = 'http://127.0.0.1:5000/add'
        response = requests.get(api_url,params=params)
        print(response.content)

    def do_Quit(self, line):
        return True

if __name__ == '__main__':
    KVShell().cmdloop()