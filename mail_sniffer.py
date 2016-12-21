import scapy

def packet_callback(packet):
    print packet.show()

sniff(prn=packet_callback,count=1)
