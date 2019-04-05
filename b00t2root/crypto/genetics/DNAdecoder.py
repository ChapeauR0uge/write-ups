#!/bin/python3

import sys

dna_table = {"AAA":"a",
             "AAC":"b",
             "AAG":"c",
             "AAT":"d",
             "ACA":"e",
             "ACC":"f",
             "ACG":"g",
             "ACT":"h",
             "AGA":"i",
             "AGC":"j",
             "AGG":"k",
             "AGT":"l",
             "ATA":"m",
             "ATC":"n",
             "ATG":"o",
             "ATT":"p",
             "CAA":"q",
             "CAC":"r",
             "CAG":"s",
             "CAT":"t",
             "CCA":"u",
             "CCC":"v",
             "CCG":"w",
             "CCT":"x",
             "CGA":"y",
             "CGC":"z",
             "CGG":"A",
             "CGT":"B",
             "CTA":"C",
             "CTC":"D",
             "CTG":"E",
             "CTT":"F",
             "GAA":"G",
             "GAC":"H",
             "GAG":"I",
             "GAT":"J",
             "GCA":"K",
             "GCC":"L",
             "GCG":"M",
             "GCT":"N",
             "GGA":"O",
             "GGC":"P",
             "GGG":"Q",
             "GGT":"R",
             "GTA":"S",
             "GTC":"T",
             "GTG":"U",
             "GTT":"V",
             "TAA":"W",
             "TAC":"X",
             "TAG":"Y",
             "TAT":"Z",
             "TCA":"1",
             "TCC":"2",
             "TCG":"3",
             "TCT":"4",
             "TGA":"5",
             "TGC":"6",
             "TGG":"7",
             "TGT":"8",
             "TTA":"9",
             "TTC":"0",
             "TTG":" ",
             "TTT":"."}

valid_char = ["A", "C", "G", "T"]

def decoder(filename_IN):
    filename_OUT = "flag.txt"
    my_stream_IN = open(filename_IN,"r")
    my_stream_OUT = open(filename_OUT,"wb")

    data = my_stream_IN.read()
    data_sanitized = sanitize(data)
    
    if(len(data)%3 != 0):
        print(sys.argv[0]+": crypted message size doesn't correct, some data could be lost !")

    b = ''
    for c in data:
        if isValidChar(c):
            if(len(b) == 3):
                my_stream_OUT.write(bytes(dna_table[b], 'utf-8'))
                if isValidChar(c):
                    b = c
                else:
                    b = ''
            else:
                b += c
                
    my_stream_OUT.close()
    my_stream_IN.close()

def isValidChar(c):
    return c in valid_char 

def sanitize(d):
    d_s = d.replace(" ", "")
    d_s = d.replace("\n","")
    return d_s

def usage():
    print("Need a filename")
    print("usage:",sys.argv[0],"<filename>")
    
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        usage()
    else:
        decoder(sys.argv[1])
