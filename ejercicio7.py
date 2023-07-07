import unittest
import requests

URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'
A = 1
B=2

class TestRequest(unittest.TestCase):

    def test_request_get(self):
        parametros = {
            "a": A,
            "b": B
        }
        response = requests.get(URL, params=parametros)
        self.assertTrue(float(response.text), 3)

    def test_request_post(self):
        data = {
            "a": A,
            "b": B
        }
        response = requests.get(URL, json=data)
        self.assertTrue(float(response.json()["result"]), 3)

if __name__ =='__main__':
    unittest.main()