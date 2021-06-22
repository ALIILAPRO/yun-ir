import requests
import json

class Yun:
	def __init__(self, token: str):
		self.token = token

	def short(self, title, url):
		body = {"title": f"{title}",
				"url": f"{url}"}

		data = json.dumps(body).encode('utf8')

		headers = {'Content-Type': 'application/json',
					'X-API-Key': self.token,
					'Content-Length': str(len(data)),
					}

		req         = requests.post('https://yun.ir/api/v1/urls', data=data, headers=headers)
		if req.status_code == 200:
			req = req.json()
			# req = req['doc']['url'] for get short url

		return req
