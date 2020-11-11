import sys
from netmiko import ConnectHandler
import re
import time
def cisco_sshconnection(user_ip, user_port, user_name, user_pwd, en_pwd='none'):
	cisco_wlc = {'ip': user_ip, 'port': user_port, 'username': user_name, 'password': user_pwd, 'secret': en_pwd,
                 'device_type': 'cisco_wlc_ssh'}
	return ConnectHandler(**cisco_wlc)
# ssh connection to cisco controller AP
try:
	net_connect = cisco_sshconnection('192.168.10.10', 22, 'theatro', 'theatro+1')
except NetMikoTimeoutException as e:
	print("ssh timeout issue:", e)
	sys.exit()
#mac_file=open('mac_list.txt','r')
mac_file = open('ip.log','r')
lines = mac_file.readlines()
full_ips = ""
ips_count = 0
i = 0
while i < 1:
	for line in lines:
		ip_dict=line.split("'")[1:]
		#print ("siddarth_mac",ip_dict[0])
		if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", ip_dict[0].lower()):
			res = net_connect.send_command("config client deauthenticate {}".format(ip_dict[0]))
			if 'Client specified is unknown' in res:
				print("ERROR: mac not found in connected list", ip_dict[0])
			else:
				print("disconnected client:", ip_dict[0])
		else:
			print("ERROR: Incorrect mac address", ip_dict[0])
	time.sleep(20)
		


#for line in mac_file.readlines():
#    line = line.strip("\n")
#    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", line.lower()):
#        res = net_connect.send_command("config client deauthenticate {}".format(line))
#        #res = net_connect.send_command("config client deauthenticate e8:e8:b7:0c:b6:07")
#        if 'Client specified is unknown' in res:
#            print("ERROR: mac not found in connected list", line)
#        else:
#            print("disconnected client:", line)
#    else:
#        print("ERROR: Incorrect mac address", line)


net_connect.disconnect()



