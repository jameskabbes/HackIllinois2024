import numpy as np
import time
import socket
from src import switch as switch_module

# Pi ip = 172.16.114.228
# Cellular ip = 100.97.148.32
GPS2IP_IP = '100.97.148.32'  # Example IP, replace with actual
GPS2IP_PORT = 11123  # Default port used by GPS2IP, replace if different


def read_gps_data(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        print("Connected to GPS2IP server.")

        try:
            while True:
                data = s.recv(1024)
                if not data:
                    print("Disconnected.")
                    break
                print("Received:", data.decode())
        except KeyboardInterrupt:
            print("Stopped by user.")


if __name__ == "__main__":
    read_gps_data(GPS2IP_IP, GPS2IP_PORT)