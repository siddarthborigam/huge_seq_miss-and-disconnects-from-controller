import os
import sys
import os
import time
import random

i = 0

mac_file = open('ip.log','r')
lines = mac_file.readlines()
full_ips = ""
ips_count = 0
for line in lines:
	ip_dict=line.split("'")[1:]
	#print ip_dict[2]
	full_ips = full_ips + ip_dict[2] + " "
	ips_count = ips_count + 1
	#print "ip_1",ip_dict[1]
#print full_ips
#print ips_count
ips = str(ips_count) + " " + str(full_ips)
#print ips

while i < 1:
        n = random.randint(20,50)
        time.sleep(20)
        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
        time.sleep(20)
        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)
        time.sleep(20)
        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 random_huge_seq_miss 333 " + ips)
        time.sleep(20)
        os.system("./pkt_spoof_ext 1 50008 1 " + str(n) + " 40 1 200 voice_call 111 " + ips)

