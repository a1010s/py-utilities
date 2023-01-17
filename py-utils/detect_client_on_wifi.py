import os
from time import sleep


# client counter
number_clients = 0 

# first scan, initial number
initial_scan = int(os.popen("nmap -sP 192.168.1.0/24 | grep 192 | grep -v unifi.localdomain | wc -l").read())
print(f'Initial number of clients: {initial_scan}')

# run the program:
while True:
    scan = int(os.popen("nmap -sP 192.168.1.0/24 | grep 192 | grep -v unifi.localdomain | wc -l").read())
    
    # if new client number change, notify me!
    if number_clients != scan:
        print(f'Number of clients changed: {scan}')
        number_clients = scan
        sleep(10)