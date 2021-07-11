import pickle
from flask import Flask, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
port = 5000

@app.route('/', methods=['GET'])
def kvhome():
    return "<h1>KV Store Web Server</h1>"

#To dump serialize and dump the dictionary data to a file using pickle to have persistance in the data.
def dump_data_for_cache(store):
    with open("store.pickle","wb") as handle:
        pickle.dump(store,handle,protocol=pickle.HIGHEST_PROTOCOL)

#Helper to add KV pair to our store.
@app.route('/add', methods=['POST'])
def add_value():
    global changed
    if 'key' and 'value' in request.args:
        key = str(request.args['key'])
        value = str(request.args['value'])

        #Check for the false case of empty key or value.
        if not key or not value:
            return "Error: Incomplete Input."
        else:
            store[key] = value
            dump_data_for_cache(store)
            return "Successfully added Value - %s for Key - %s" % (store[key],key)
    else:
        return "Error: Improper input."

#Helper to get the value of provided key from our store.
@app.route('/get', methods=['GET'])
def get_value():
    if 'key' in request.args:
        key = str(request.args['key'])
        if not key:
            return "Error: Empty KEY provided."
        else:
            if key in store:
                return store[key]
            else:
                return "Error: Provided key doesn't exists in the store."
    else:
        return "Error: No KEY provided."

@app.route('/get_all', methods=['GET'])
def get_all():
    return store

#Load the dumped data everytime the API starts.
datatoload = open("store.pickle","rb")
store = pickle.load(datatoload)

http_server = WSGIServer(('127.0.0.1',port),app)
http_server.serve_forever()