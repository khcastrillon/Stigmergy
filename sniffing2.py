from scapy.all import *

pkts=sniff(filter="ip", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
pkts.summary()