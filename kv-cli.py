import cmd
import requests
import socket
import errno
from socket import error as socket_error

server_ip = '127.0.0.1'
server_port = 12345

class KVShell(cmd.Cmd):
    intro = "CLI Client to consume the KV Web API. Type help or ? to list commands. To exit press 'Ctrl + D' or fire 'quit' command."
    prompt = 'kvstore> '

#CLI command to retrieve the value of a particular key.
    def do_get(self, key):
        if len(key.split()) == 1:
            params = {'key': key}
            api_url = 'http://127.0.0.1:5000/get'
            response = requests.get(api_url,params=params)
            print(response.content)
        else:
            print("Error: Incorret Input! Please follow the syntax - get <key>")

#Description for the get function mentioned above.
    def help_get(self):
        print("Get the value of the provided key.")
        print("Syntax - get <key>")

#CLI commnd to add value for a particular key in the KV Store.
    def do_set(self,input):
        global server_port
        global server_ip
        if len(input.split()) == 2:
            key,value = [str(s) for s in input.split()]
            params = {'key': key, 'value': value}
            api_url = 'http://127.0.0.1:5000/add'
            response = requests.post(api_url,params=params)
            print(response.content)
            try:
                sock = socket.socket()
                server_address = (server_ip,server_port)
                sock.connect(server_address)
                sock.sendall(response.content)
            except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
                    raise serr
        else:
            print("Error: Incorrect Input! Please follow the syntax - set <key> <value>")

#Description for the set function mentioned above.
    def help_set(self):
        print("Set the value of the provided key.")
        print("Syntax - set <key> <value>")

#CLI command to subscribe to the changes to the KV store.
    def do_watch(self,line):
        """Subcribe to the changes happening in the KV store."""
        global server_ip
        global server_port
        sock = socket.socket()
        sock.bind((server_ip,server_port))
        sock.listen(5)
        while True: 
            client,addr = sock.accept()
            print(client.recv(1024))
            client.close()

#CLI command to exit from the CLI shell.            
    def do_quit(self, line):
        """To exit the shell."""
        return True

#Ctrl + D to exit from the CLI shell.
    def do_EOF(self, line):
        """To exit the shell."""
        return True

if __name__ == '__main__':
    KVShell().cmdloop()