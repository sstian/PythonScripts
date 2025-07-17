import unittest
import json
from main import app

class LoginTest(unittest.TestCase):
    def setUp(self):
        # 设置fask工作在测试模式
        # app.config["TESTING"] = True
        app.testing = True

        # 创建web请求的客户端，使用flask提供的
        self.client = app.test_client()

    def tearDown(self):
        pass


    def test_wrong_username_password(self):
        result = self.client.post("/login", data={"username": "admin", "password": "admin"})
        response = result.data
        res = json.loads(response)

        self.assertIn("code", res)
        self.assertEqual(res["code"], 2)

if __name__ == "__main__":
    unittest.main()
