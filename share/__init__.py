import os

def readData(parentfile: str, data: str) -> object:
    sampleFile = os.path.dirname(parentfile) + "\\" + data
    with open(sampleFile, 'r') as fileIn:
        outfile = fileIn.read().split("\n\n")
    return outfile


def parseData(parentfile: str, data: str) -> object:
    infile = readData(parentfile, data)
    outfile = []
    for entry in infile:
        entry = entry.replace("\n", "").replace("\r", "") # remove new lines 
        outfile.append(entry)   
    return outfile