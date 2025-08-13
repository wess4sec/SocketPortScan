import socket
import re

# Regex pattern to recognize IPv4 addresses
ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# Regex pattern to extract port range (e.g., 10-100)
port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")

# Initialize port numbers
port_min = 0
port_max = 65535

# UI header
print(r"""****************************************************************

   _____                  _     _  _    ___  _  _   
  / ____|                (_)   | || |  / _ \| || |  
 | |  __  ___ _ __  _   _ _ ___| || |_| | | | || |_ 
 | | |_ |/ _ \ '_ \| | | | / __|__   _| | | |__   _|
 | |__| |  __/ | | | |_| | \__ \  | | | |_| |  | |  
  \_____|\___|_| |_|\__,_|_|___/  |_|  \___/   |_|  
""")

print("\n****************************************************************")

open_ports = []

# Ask user to input the IP address
while True:
    ip_add_entered = input("\nPlease enter the IP address you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid IP address. GREAT!")
        break
    else:
        print("Invalid IP address. Try again.")

# Ask user to input port range
while True:
    print("Please enter the range of ports to scan in format: <int>-<int> (e.g., 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
    else:
        print("Invalid port range. Try again.")

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    try:
        # Create a TCP socket using IPv4
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # timeout for connection
            s.connect((ip_add_entered, port))
            open_ports.append(port)
    except:
        pass  # ignore closed or filtered ports

# Display the open ports
for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")
