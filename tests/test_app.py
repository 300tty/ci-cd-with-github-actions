# test/test_app.py

import unittest
from app import app, items

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        items.clear()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        response = self.client.post('/add', data=dict(item='New Test Item'), follow_redirects=True)
        self.assertIn('New Test Item', response.get_data(as_text=True))

    def test_delete_item(self):
        self.client.post('/add', data=dict(item='New Test Item'), follow_redirects=True)
        response = self.client.get('/delete/0', follow_redirects=True)
        self.assertNotIn('New Test Item', response.get_data(as_text=True))

    def test_update_item(self):
        self.client.post('/add', data={'item': 'old Item'}, follow_redirects=True)
        response = self.client.get('/')
        self.assertIn('old Item', response.get_data(as_text=True))
        response = self.client.post('/update/0', data={'new_item': 'Updated Item'}, follow_redirects=True)
        self.assertNotIn('old Item', response.get_data(as_text=True))
        self.assertIn('Updated Item', response.get_data(as_text=True))
