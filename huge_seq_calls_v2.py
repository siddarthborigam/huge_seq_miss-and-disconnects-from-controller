import os
import sys
import os
import time
import random
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko import ConnectHandler

#i = 0

#mac_file = open('ip.log','r')
#lines = mac_file.readlines()
#full_ips = ""
#ips_count = 0
#for line in lines:
#	ip_dict=line.split("'")[1:]
#	#print ip_dict[2]
#	full_ips = full_ips + ip_dict[2] + " "
#	ips_count = ips_count + 1
#	#print "ip_1",ip_dict[1]
##print full_ips
##print ips_count
#ips = str(ips_count) + " " + str(full_ips)
##print ips

#while i < 1:
#        n = random.randint(20,50)
#        time.sleep(20)
#        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
#        time.sleep(20)
#        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)
#        time.sleep(20)
#        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
#        time.sleep(20)
#        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)


#new script
def call():
	try:
		net_connect = cisco_sshconnection('192.168.10.10', 22, 'theatro', 'theatro+1')
	except NetMikoTimeoutException as e:
		print("ssh timeout issue:", e)
		sys.exit()
	print("connection success")
	#out_file = open('ip.log', 'w')
	#mac_list=mac_read.values.tolist()
	ip_count=mac_file = open('ip.log','r')
	mac_file = open('ip.log','r')
	lines = mac_file.readlines()
	full_ips = ""
	ip_count = 0
	full_ips = ""
	cmd = ""
	for line in lines:
		mac_id = line.split("'")[0:][1]
		#print("sid_mac_id",mac_id)
		#cmd = "show client detail " + mac_id
		cmd="show client detail %s" %str(mac_id)
		print(cmd)
		#if mac_id in cmd:
		#	print("mac_id_available")
		res = net_connect.send_command(cmd)
		matched_lines = [line for line in res.split('\n') if "IP Address....." in line]
		print("match_lies %s" %matched_lines)
		#if ("IP Address" in matched_lines):
		if (len(matched_lines)!=0):
			ip_add=matched_lines[0].split("IP Address....................................... ")[1]
			print("%s:%s" %(matched_lines, ip_add))
			if ((ip_add != "0.0.0.0" ) and ("Unknown" not in ip_add)):
				full_ips = full_ips + ip_add + " "
				#str_ip=("\'%s\':\'%s\'\n" %(mac_id, ip_add))
				#print(str_ip)
				#out_file.writelines(str_ip)
				ip_count = ip_count + 1
	ips = str(ip_count) + " " + str(full_ips)
	print("siddarth_ips",ips)
	n = random.randint(20,50)
	time.sleep(20)
	os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
	time.sleep(20)
	os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)
	time.sleep(20)
	os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
	time.sleep(20)
	os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)

	net_connect.disconnect()
	#out_file.flush()
	#out_file.close()
	#return ip_count 

def cisco_sshconnection(user_ip, user_port, user_name, user_pwd, en_pwd='none'):
        cisco_wlc = {'ip': user_ip, 'port': user_port, 'username': user_name, 'password': user_pwd, 'secret': en_pwd,
                                 'device_type': 'cisco_wlc_ssh'}
        return ConnectHandler(**cisco_wlc)

i = 0
while i < 1:	
	call()
	time.sleep(20)

