try:
    import scapy.all as scapy
except ImportError:
    import scapy
try:
    # This import works from the project directory
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http
from scapy.all import *

pcap = rdpcap('C:/Desktop/detect.pcap')[TCP]
for i in range(len(pcap)):
    try:
        raw = str(pcap[i][Raw])
        # if 'a=' in raw and 'b=' in raw and 'c=' and 'd=' in raw:
        if 'wangyang' in raw:
            print pcap[i][Raw]
            print pcap[i]['IP'].src,'----',pcap[i]['IP'].dst
            # print(raw)
            # print(raw[0:raw.find('a=')])
    except:
        continue
