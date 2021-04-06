#!/usr/bin/env python

Disk1 = open("data/DISK1.bin",'rb')
Disk2 = open("data/DISK2_recovered.bin",'rb')
Disk3 = open("data/DISK3.bin",'rb')

Disk = open("data/DISK.img", 'wb')

cpt = 3

while(1):
    b1 = Disk1.read(1)
    b2 = Disk2.read(1)
    b3 = Disk3.read(1)
    if cpt == 3:
        Disk.write(b1)
        Disk.write(b2)
    elif cpt == 2:
        Disk.write(b1)
        Disk.write(b3)
    elif cpt == 1:
        Disk.write(b2)
        Disk.write(b3)

    cpt = cpt-1
    if(cpt == 0):
        cpt = 3
    print("-",b1)
    if not b1:
        print("end")
        Disk1.close()
        Disk2.close()
        Disk3.close()
        Disk.close()
        break