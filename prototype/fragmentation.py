from scapy.all import IP, ICMP, send, fragment

def send_fragmented_packet(destination, payload, frag_size=8):
    ip_pkt = IP(dst=destination)
    icmp_pkt = ICMP()
    frags = fragment(payload, frag_size)

    for frag in frags:
        packet = ip_pkt/frag/icmp_pkt
        send(packet, verbose=False)


destination_ip = "target_ip"
payload_data = b"payload_here"  

send_fragmented_packet(destination_ip, payload_data)
