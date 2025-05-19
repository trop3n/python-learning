import requests

base_url = "http://localhost:40000/v1"

def connect_to_propresenter():
    try:
        response = requests.get(f"{base_url}"/status")
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

if connect_to_propresenter():
    print("Connected to ProPresenter")
else:
    print("Failed to connect")