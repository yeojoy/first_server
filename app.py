from flask import Flask, jsonify

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET = used to send data back only

# POST /store data: {name:""}
@app.route('/store', methods=['POST'])
def create_store():
    pass
# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5050/store/some_name
def get_store(name):
    pass
# GET /store

@app.route('/store') # 'http://127.0.0.1:5050/store/some_name
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # 'http://127.0.0.1:5050/store/some_name
def get_item_in_store(name):
    pass

#@app.route('/json')
#def summary():
#    d = make_summary()
#    return jsonify(d)

#def make_summary():
#    return { 'hi':'hello' }

app.run(host='0.0.0.0', port=5050)
