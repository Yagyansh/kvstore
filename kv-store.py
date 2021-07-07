import flask
import pickle
from flask import Flask, redirect, url_for, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def kvhome():
    return "<h1>KV Store Web Server</h1>"

#To dump serialize and dump the dictionary data to a file using pickle to have persistance in the data.
def dump_data_for_cache(store):
    with open("/home/yagyanshkumar/Grofers-Assignment/store.pickle","wb") as handle:
        pickle.dump(store,handle,protocol=pickle.HIGHEST_PROTOCOL)

#Helper to add KV pair to our store.
@app.route('/add', methods=['GET'])
def add_value():
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
    else:
        return "Error: No KEY provided."
    return store[key]

#Load the dumped data everytime the API starts.
datatoload = open("/home/yagyanshkumar/Grofers-Assignment/store.pickle","rb")
store = pickle.load(datatoload)
print(store)
app.run()