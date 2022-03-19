#!usr/bin/python
import os
import subprocess

print("Installing...")

subprocess.call('sudo dnf install -y wireguard-tools', shell=True)
subprocess.call('sudo mkdir -p /etc/wireguard/', shell=True)

pub = os.popen('wg genkey | sudo tee /etc/wireguard/server_private.key | wg pubkey | sudo tee /etc/wireguard/server_public.key')
publickey = pub.read()
print("Public key = " + publickey)

pri = os.popen('sudo cat /etc/wireguard/server_private.key')
privatekey = pri.read()
print("Public Key = " + privatekey)

ip = os.popen('hostname -I')
ipaddr = ip.read()
ip = ipaddr[:-2] + "/24"
print("IP = " + ip)

wg0conf = "sudo sh -c \"echo -e \'[Interface]\nAddress = 10.0.0.1\nSaveConfig = true\nPostUp = firewall-cmd --zone=public --add-port 51820/udp && firewall-cmd --zone=public --add-masquerade\nPostDown = firewall-cmd --zone=public --remove-port 51820/udp && firewall-cmd --zone=public --remove-masquerade\nListenPort = 51820\nPrivateKey = " + privatekey + "\' > /etc/wireguard/wg0.conf\""
subprocess.call(wg0conf, shell=True)

subprocess.call('sudo chmod 600 /etc/wireguard/ -R', shell=True)

sysctlconf = "sudo sh -c \"echo -e \'\nnet.ipv4.ip_forward = 1\nnet.ipv6.conf.all.forwarding = 1\' > /etc/sysctl.conf\""
subprocess.call(sysctlconf, shell=True)
subprocess.call('sudo sysctl -p', shell=True)

rule = "sudo firewall-cmd --permanent --add-rich-rule=\'rule family=\"ipv4\" source address=\"" + ip + "\" masquerade\'"
subprocess.call(rule, shell=True)

subprocess.call('sudo systemctl reload firewalld', shell=True)
subprocess.call('sudo dnf install -y bind && sudo systemctl enable named && sudo systemctl start named', shell=True)

name = "sed -i \'s/serverIp/" + ipaddr[:-2] + "/g\' ./named.conf"
subprocess.call(name, shell=True)

namedconf = "sudo cp -f ./named.conf /etc/named.conf"
subprocess.call(namedconf, shell=True)

rule = "sudo systemctl restart named&&sudo firewall-cmd --zone=public --permanent --add-rich-rule=\'rule family=\"ipv4\" source address=\"" + ip + "\" accept\'"
subprocess.call(rule, shell=True)

subprocess.call('sudo firewall-cmd --permanent --add-port=51820/udp&&sudo systemctl reload firewalld', shell=True)
subprocess.call('sudo wg-quick up /etc/wireguard/wg0.conf&&sudo wg-quick down /etc/wireguard/wg0.conf', shell=True)
subprocess.call('sudo systemctl enable wg-quick@wg0.service', shell=True)
subprocess.call('sudo systemctl start wg-quick@wg0.service&&sudo systemctl stop wg-quick@wg0.service', shell=True)
subprocess.call('sudo wg-quick up /etc/wireguard/wg0.conf&&sudo wg', shell=True)

print("Server Key = " + publickey)
print("Server IP = " + ipaddr[:-2])
