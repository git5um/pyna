#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue

def ssh_action(our_commands, sshsession):
    resp = cmdissue(our_commands, sshsession)
    if resp != "":
      print(resp)


def main():
  ## create session object
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

  ## create SSH connection
    sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)
    
    print("Enter 'q' to quit")
    user_input = ''
  
    while user_input != 'q':
        our_commands = str(input('Please enter text to pass? '))
        if our_commands != '':
            ssh_action(our_commands, sshsession)
            continue
        elif our_commands == 'q':
            break
        else:
            continue


if __name__ == '__main__':
  main()

