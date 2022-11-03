import requests

def get_ip():
	try:
		response = requests.get(url='https://ifconfig.me/all.json').json()
		return response['ip_addr']
	except requests.exceptions.ConnectionError:
		return	'Check connection!'