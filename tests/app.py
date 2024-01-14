# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get('item')
    items.append(item)
    return jsonify(item), 201
@app.route('/')
def index():
    return "Welcome to the Flask App!"

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if index < len(items):
        item = items.pop(index)
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
