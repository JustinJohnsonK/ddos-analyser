import pandas as pd
import pyshark
import csv
import time
from timeit import default_timer as timer

def main():
    allowed_IP = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
    fileName = 'app/LiveAnn.csv'
    capture = pyshark.LiveCapture(interface='any')
    capture.sniff_continuously(packet_count=10)
    # for packet in capture.sniff_continuously(packet_count=None):
    #     print('Just arrived:', packet)
    try:
        while True:                                      
            csv_interval_gather(capture, allowed_IP)
    except KeyboardInterrupt:
        pass   
    
    packets = pd.read_csv(fileName, sep='","')
    return(packets)


def get_ip_layer_name(pkt): #allows the program to differentiate between ipv4 and ipv6, needed for correct parsing of packets
    for layer in pkt.layers:
        if layer._layer_name == 'ip':
            return 4
        elif layer._layer_name == 'ipv6':
            return 6

def csv_interval_gather(cap, allowed_IP): # creates/rewrites 'Live.csv' file with 30 second intervals- writes header row - goes through packets, writing a row to the csv for each packet
    start_time = time.time()
    with open ('app/LiveAnn.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Highest Layer', 'Transport Layer', 'Source IP', 'Dest IP', 'Source Port', 'Dest Port','Packet Length', 'Packets/Time'])

        i = 0
        start = timer()
        for pkt in cap:
            end = timer()
            if (end - start < 30):
                try:
                    if pkt.highest_layer != 'ARP':
                        print("Packets Collected:", i)
                        if pkt.highest_layer != 'ARP':
                            ip = None
                            ip_layer = get_ip_layer_name(pkt)
                            if ip_layer == 4:
                                ip = pkt.ip
                                #ipv = 0 # target test
                                if pkt.transport_layer == None:
                                    transport_layer = 'None'
                                else:
                                    transport_layer = pkt.transport_layer
                            elif ip_layer == 6:
                                ip = pkt.ipv6
                                #ipv = 1 # target test
                            try:
                                if ip.src not in allowed_IP:
                                        ipcat = 1
                                else:
                                        ipcat = 0
                                filewriter.writerow([pkt.highest_layer, transport_layer, ipcat, ip.dst, pkt[pkt.transport_layer].srcport, pkt[pkt.transport_layer].dstport,pkt.length, i/(time.time() - start_time)])
                                print ("Time: ", time.time() - start_time)
                                i += 1
                            except AttributeError:
                                if ip.src not in allowed_IP:
                                        ipcat = 1
                                else:
                                        ipcat = 0
                                filewriter.writerow([pkt.highest_layer, transport_layer, ipcat, ip.dst, 0, 0, pkt.length, i/(time.time() - start_time)])
                                print ("Time: ", time.time() - start_time)
                                i += 1

                        else:
                            if pkt.arp.src_proto_ipv4 not in allowed_IP:
                                    ipcat = 1
                            else:
                                    ipcat = 0
                            arp = pkt.arp
                            filewriter.writerow([pkt.highest_layer , transport_layer, ipcat, arp.dst_proto_ipv4, 0, 0, pkt.length, i/(time.time() - start_time)])
                            print ("Time: ", time.time() - start_time)
                            i += 1
                except (UnboundLocalError, AttributeError) as e:
                        pass
            else:
                return

main()


# # reads the input file and transforms it. 
# import pandas as pd
# import csv
# import pyshark
# import netifaces

# class read_file:

#     """
#     read the csv dataset
#     extract necessary details from the dataset
#     """  

#     def __init__(self, filename):
#         int = netifaces.interfaces()

#         self.cap = int_choice()
#         self.filename = 'LiveAnn.csv'
    

#     def openFile(self):
#         packets = pd.read_csv(self.fileName, sep='","')
#         return(packets)
