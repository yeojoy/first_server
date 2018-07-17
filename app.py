from flask import Flask
from flask import jsonify
from flask import request

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
    request_data = request.get_json() 
    new_store = {
        'name': request_data['name'],
        'item': [
        ]
    }

    stores.append(new_store)
    return jsonify({'new_store':new_store})

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5050/store/some_name
def get_store(name):
    # Iterate over stores
    for store in stores:
        if store['name'] == name:
            # if the store name matches, return it
            return jsonify({'store': store})

    # If none match, return an error message
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store') # 'http://127.0.0.1:5050/store/some_name
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price: }
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            #item = store['item']
            #item['name'] = request_data['name']
            #item['price'] = request_data['price']
            item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            stores.append(item)

            return jsonify({'new_item': item})

    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # 'http://127.0.0.1:5050/store/some_name
def get_item_in_store(name):
    for store in sotres:
        if store['name'] == name:
            return jsonify({'items': store['item']})

    return jsonify({'message': 'store not found'})

#@app.route('/json')
#def summary():
#    d = make_summary()
#    return jsonify(d)

#def make_summary():
#    return { 'hi':'hello' }

app.run(host='0.0.0.0', port=5050)
