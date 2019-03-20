# reads the input file and transforms it. 
import pandas as pd

class read_file:

    """
    read the csv dataset
    extract necessary details from the dataset
    """  

    def __init__(self, filename):
        self.filename = 'packets.csv'

    def openFile(self):
        packets = pd.read_csv(self.fileName, sep='","')
        return(packets)
