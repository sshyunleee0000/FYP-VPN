from django.contrib import admin
import os, subprocess
from .models import Peer, Member

class PeerAdmin(admin.ModelAdmin):
    fields = ['p_title', 'p_key', 'p_ip', 'member']
    list_display = ('p_title', 'p_al', 'date_created')
    actions = ['make_allowed', 'make_notallowed']
    
    @admin.action(description='Mark selected peers as allowed')
    def make_allowed(modeladmin, request, queryset):
        queryset.update(p_al=1)
        pri = os.popen('sudo cat /etc/wireguard/server_private.key')
        privatekey = pri.read()
        peer = Peer.objects.filter(p_al=1).values()
        text = "[Interface]\nAddress = 10.0.0.1\nSaveConfig = true\nPostUp = firewall-cmd --zone=public --add-port 51820/udp && firewall-cmd --zone=public --add-masquerade\nPostDown = firewall-cmd --zone=public --remove-port 51820/udp && firewall-cmd --zone=public --remove-masquerade\nListenPort = 51820\nPrivateKey = " + privatekey
        count = len(peer)
        if count > 1:
            for i in range(count-1):
                key = peer[i+1]['p_key']
                text = text + "\n[Peer]\nPublickey = " + key + "\nAllowedIPs = 0.0.0.0/0"
        wg0conf = "sudo sh -c \"echo -e \'" + text + "\' > /etc/wireguard/wg0.conf\""
        subprocess.call('sudo wg-quick down /etc/wireguard/wg0.conf', shell=True)
        subprocess.call(wg0conf, shell=True)
        subprocess.call('sudo wg-quick up /etc/wireguard/wg0.conf', shell=True)
    
    @admin.action(description='Mark selected peers as not allowed')
    def make_notallowed(modeladmin, request, queryset):
        queryset.update(p_al=0)
        pri = os.popen('sudo cat /etc/wireguard/server_private.key')
        privatekey = pri.read()
        peer = Peer.objects.filter(p_al=1).values()
        text = "[Interface]\nAddress = 10.0.0.1\nSaveConfig = true\nPostUp = firewall-cmd --zone=public --add-port 51820/udp && firewall-cmd --zone=public --add-masquerade\nPostDown = firewall-cmd --zone=public --remove-port 51820/udp && firewall-cmd --zone=public --remove-masquerade\nListenPort = 51820\nPrivateKey = " + privatekey
        count = len(peer)
        if count > 1:
            for i in range(count - 1):
                key = peer[i + 1]['p_key']
                text = text + "\n[Peer]\nPublickey = " + key + "\nAllowedIPs = 0.0.0.0/0"
        wg0conf = "sudo sh -c \"echo -e \'" + text + "\' > /etc/wireguard/wg0.conf\""
        subprocess.call('sudo wg-quick down /etc/wireguard/wg0.conf', shell=True)
        subprocess.call(wg0conf, shell=True)
        subprocess.call('sudo wg-quick up /etc/wireguard/wg0.conf', shell=True)


admin.site.register(Peer, PeerAdmin)
admin.site.register(Member)

