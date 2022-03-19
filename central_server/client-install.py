#!usr/bin/python
import os
import subprocess

print("Installing...")

subprocess.call('sudo dnf install -y wireguard-tools', shell=True)
subprocess.call('sudo mkdir -p /etc/wireguard/', shell=True)

pub = os.popen('wg genkey | sudo tee /etc/wireguard/client_private.key | wg pubkey | sudo tee /etc/wireguard/client_public.key')
publickey = pub.read()
print("Public key = " + publickey)

pri = os.popen('sudo cat /etc/wireguard/client_private.key')
privatekey = pri.read()
print("Private Key = " + privatekey)

addr = input("Type the client address: ")
serverKey = input("Type the Server key: ")
serverIp = input("Type the Server Ip: ")

wg0conf = "sudo sh -c \"echo -e \'[Interface]\nAddress = " + addr + "\nPrivateKey = " + privatekey + "\nListenPort = 51820\n\n[Peer]\nPublickey = " + serverKey + "\nAllowedIPs = 0.0.0.0/0\nEndpoint = " + serverIp + ":51820\' > /etc/wireguard/wg0.conf\""
subprocess.call(wg0conf, shell=True)

subprocess.call('sudo chmod 600 /etc/wireguard/ -R', shell=True)
print("Address = " + addr)
print("Publickey = " + publickey)
