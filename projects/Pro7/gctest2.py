import socket
import requests

# GlobalCache device settings
HOST = "0.0.0.0"
PORT = 4999

# URL to send the GET request to
TARGET_URL = "http://example.com/api/control" # replace with your target URL

def parse_globalcache_data(data):
    """
    Parse the GlobalCache output to detect slide changes.
    Example: If the data is "SLIDE: 1", return the slide number.
    """
    if data.startswith(b"SLIDE:"):
        return int(data.split(b":")[1])
    return None

def send_get_request(slide_number):
    """
    Send a GET request to the target URL with the slide number as a parameter.
    """
    params = {"slide": slide_number} # Add any required parameters
    try:
        response = requests.get(TARGET_URL, params=params)
        if response.status_code == 200:
            print(f"GET request successful for slide {slide_number}")
        else:
            print(f"Failed to send GET request: {response.status_code}")
    except Exception as e:
        print(f"Error sending GET request: {e}")

# # Create a TCP socket to list for GlobalCache output
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Listening for GlobalCache output on {HOST}:{PORT}...")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected to {client_address}")

            # Receive data
            data = client_socket.recv(1024) # Adjust buffer size as needed
            if not data:
                break

            # Parse the data to detect slide changes
            slide_number = parse_globalcache_data(data)
            if slide_number is not None:
                print(f"Slide change detected: Slide {slide_number}")

                # Send a GET request to the target URL
                send_get_request(slide_number)