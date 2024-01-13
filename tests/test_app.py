# test/test_app.py

import unittest
from app import app, items

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # 创建一个测试客户端
        self.client = app.test_client()
        # 在测试环境中运行应用
        self.client.testing = True
        # 清空测试用的 in-memory 数据库
        items.clear()

    def test_home_page(self):
        # 发送GET请求到首页
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        # 测试添加项目功能
        response = self.client.post('/add', data=dict(item='New Test Item'), follow_redirects=True)
        self.assertIn('New Test Item', response.get_data(as_text=True))

    def test_delete_item(self):
        # 先添加一个项目然后再删除
        self.client.post('/add', data=dict(item='New Test Item'), follow_redirects=True)
        response = self.client.get('/delete/0', follow_redirects=True)
        self.assertNotIn('New Test Item', response.get_data(as_text=True))

    def test_update_item(self):
        # 首先添加一个名为 "old Item" 的项目
        self.client.post('/add', data={'item': 'old Item'}, follow_redirects=True)
        
        # 确认 "old Item" 现在在列表中
        response = self.client.get('/')
        self.assertIn('old Item', response.get_data(as_text=True))

        # 更新 "old Item" 为 "Updated Item"
        response = self.client.post('/update/0', data={'new_item': 'Updated Item'}, follow_redirects=True)
        
        # 检查 "old Item" 不在响应中
        self.assertNotIn('old Item', response.get_data(as_text=True))
        
        # 确认 "Updated Item" 现在在列表中
        self.assertIn('Updated Item', response.get_data(as_text=True))
