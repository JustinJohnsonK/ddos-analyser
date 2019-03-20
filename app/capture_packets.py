import pyshark 
import pandas as pd

class Capture_packets:

    def __init__(self):
        print("Captures Packets")

    def capturePacket():
        capture = pyshark.LiveCapture(interface='en0')

        for packet in capture.sniff_continuously(packet_count=10):
            print('Just arrived:', packet)
    
    def readfile():
        data = pd.read_csv('packets.csv')
        print(data)
                
        # capture.pd.to_csv(packet_file.csv.append())