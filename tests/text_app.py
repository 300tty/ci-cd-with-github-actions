# test_app.py
import unittest
from app import app, items

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Clear the items list before each test
        items.clear()

    def test_get_items_empty(self):
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_item(self):
        response = self.app.post('/items', json={'item': 'test item'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, 'test item')
        self.assertEqual(items, ['test item'])

    def test_delete_item(self):
        items.append('test item')
        response = self.app.delete('/items/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, 'test item')
        self.assertEqual(items, [])

    def test_delete_item_not_found(self):
        response = self.app.delete('/items/0')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Item not found"})

    def test_integration_add_and_delete_item(self):
        add_response = self.app.post('/items', json={'item': 'integration test item'})
        self.assertEqual(add_response.status_code, 201)
        delete_response = self.app.delete('/items/0')
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response.json, 'integration test item')
        get_response = self.app.get('/items')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json, [])

if __name__ == '__main__':
    unittest.main()
