import unittest
from app import app, items

class UnitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        items.clear()

    def test_add_item(self):
        response = self.app.post('/add', data=dict(item='Unit Test Item'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Unit Test Item', items)

    def test_delete_item(self):
        self.app.post('/add', data=dict(item='Unit Test Item'), follow_redirects=True)
        self.assertIn('Unit Test Item', items)
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Unit Test Item', items)

if __name__ == '__main__':
    unittest.main()
