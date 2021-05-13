#!/usr/bin/env python3

import netifaces

# Lookup MAC address with user provided IP address

def ip_get(user_input):
    print('Here is the MAC address associated with the IP address you entered')
    for iface in netifaces.interfaces():
        if user_input == (netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']):
            print((netifaces.ifaddresses(iface)[netifaces.AF_LINK])[0]['addr'])

# Lookup MAC address with user provided adapter name

def an_get(user_input):
    print('Here is the MAC address associated with the adapter name you entered')
    print((netifaces.ifaddresses(user_input)[netifaces.AF_LINK])[0]['addr'])

def main():

    ip_addresses = [netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr'] for iface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(iface)]

    print('*** INSTRUCTIONS ***')
    print('Enter IP address or adapter name to lookup corresponding MAC address')
    print("Press 'q' to quit")
    
    user_input = ''
  
    while user_input != 'q':
        user_input = str(input('What would you like to lookup? '))
        if user_input in (netifaces.interfaces()):
            an_get(user_input)
            continue
        elif user_input in ip_addresses:
            ip_get(user_input)
            continue
        elif user_input == 'q':
            break
        else:
            print('Invalid input')
            continue

if __name__ == "__main__":
    main()
