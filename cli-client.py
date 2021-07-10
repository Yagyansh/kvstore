import click
import requests


#@click.group()
#def apis():
#    """A CLI wrapper for the KV API."""

@click.option('--get',type=str)
@click.command()
def get_item(get):
    params = {'key': get}
    api_url = 'http://127.0.0.1:5000/get'
    response = requests.get(api_url,params=params)
    print(response.content)

@click.option('--set',nargs=2,type=str)
@click.command()
def add_item(set):
    key,value = set
    params = {'key': key, 'value': value}
    api_url = 'http://127.0.0.1:5000/add'
    response = requests.get(api_url,params=params)
    print(response.content)

if __name__ == '__main__':
    get_item()
    add_item()

