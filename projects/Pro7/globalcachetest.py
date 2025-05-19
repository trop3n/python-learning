import socket

# GlobalCache device settings
HOST = "0.0.0.0"
PORT = 4999

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Listening for GlobalCache output on {HOST}:{PORT}...")

    while True:
        # accept a connection
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connected to {client_address}")

            # Receive data
            data = client_socket.recv(1024) # Adjust buffer size as needed
            if not data:
                break

            # Process the data
            print(f"Received data: {data.decode('utf-8')}")

            # Example: Check if the data indicates a slide change
            if "slide_change" in data.decode('utf-8').lower():
                print("Slide change detected!")
                # Add custom logic here

def parse_globalcache_data(data):
    # Example: Parse a serial command like "SLIDE:1"
    if data.startswith(b"SLIDE:"):
        slide_number = int(data.split(b":")[1])
        print(f"Slide number: {slide_number}")
        return slide_number
    return None

# Use this function in the socket listener
parsed_data = parse_globalcache_data(data)
if parsed_data:
    print(f"Parsed data: {parsed_data}")
