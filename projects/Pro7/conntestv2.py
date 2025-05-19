import requests

# ProPresenter API Details
base_url = "http://<ProPresenter_IP>:<port>/api/v1"
endpoint = "/path/to/endpoint" # replace with endpoint
headers = {
    "Authorization": "Bearer <API_KEY>",
    "Content-Type": "application/json"
}

# make a GET request
response = requests.get(f"{base_url}{endpoint}", headers=headers)

if response. status_code == 200:
    data = response.json()
    print("Response:", data)
else:
    print("Failed to fetch data:", response.status_code, response.text)