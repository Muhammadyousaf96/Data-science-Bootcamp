from flask import Flask, jsonify, request

app = Flask(__name__)

# initial data in my todolist
items = [
    {'id': 1, 'name': 'item1', 'description': 'this is item1'},
    {'id': 2, 'name': 'item2', 'description': 'this is item2'}
]

# home route
@app.route('/')
def home():
    return "Welcome to the Todo List API"


# 🔍 GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# 🔍 GET single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)


# 🟢 CREATE new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()

    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': data.get('name'),
        'description': data.get('description')
    }

    items.append(new_item)
    return jsonify(new_item), 201


# 🔄 UPDATE existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])

    return jsonify(item)


# ❌ DELETE item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items

    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({'error': 'Item not found'}), 404

    items = [item for item in items if item['id'] != item_id]

    return jsonify({'message': 'Item deleted'})


# run app
if __name__ == '__main__':
    app.run(debug=True)