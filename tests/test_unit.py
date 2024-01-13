# tests/test_unit.py
import unittest
from app import app, items

class UnitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        items.clear()  

    def test_add_item(self):
        with self.app:
            response = self.app.post('/add', data=dict(item='Test Item'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('Test Item', items)  

    def test_delete_item(self):
        with self.app:
            self.app.post('/add', data=dict(item='Test Item'), follow_redirects=True)
            self.assertIn('Test Item', items) 
            response = self.app.get('/delete/0', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertNotIn('Test Item', items)  

if __name__ == '__main__':
    unittest.main()
