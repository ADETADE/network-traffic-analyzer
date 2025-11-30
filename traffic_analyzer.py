from scapy.all import sniff

def packet_callback(packet):
    print(f"{packet.summary()}")

# Capture first 20 packets
sniff(prn=packet_callback, count=20)

