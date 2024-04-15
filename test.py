import requests
import time

def send_request_for_active_website(url, interval):
	while True:
		try:
			response = requests.get(url)
			if response.status_code == 200:
				print(f"Request to {url} successful.")
			else:
				print("Request failed: Code {response.status_code}.")
		except requests.RequestExeption as e:
			print(f"Request to {url} failed: {str(e)}")
		time.sleep(interval)

url = "https://www.google.com/"
interval = 5
send_request_for_active_website(url, interval)