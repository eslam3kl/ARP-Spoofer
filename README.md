# ARP-Spoofer

**Welcome** to my new tool ARP Spoofer <3 

This tool is used to be Man In The Middle Attack (MITM), or in other words by using this tool you'll say to the victim machine: Hey! My MAC address is the MAC of the router. And say to the router: Hey! My MAC address is the MAC of the victim machine. 


By this way the packets which send to the router or recieved by it will pass at first on your machine. 

Now you're MITM, congrats :")

__________________________________

**Usage**

python arp_spoofer.py -v (victim_ip) -r (router_ip) 

Ex.

python arp_spoofer.py -v 192.168.1.19 -r 192.168.1.1 



**Note**

If you don't specify the router and the victim IPs the packets will send to ip 0.0.0.0 (Nothing IP)
