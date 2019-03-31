#!/bin/bash

if [ $# != "1" ]
then
    echo -e "usage: $0 <filename>\nNeed a filename!"
else
    cp $1 data.tmp
    filename=data.tmp
    
    # Formatage du fichier pour gnuplot
    sed -i "s/;/\n/g" $filename
    cut -d:  -f1-2 < $filename > tmp
    cp tmp $filename
    sed -i "s/:/ /g" $filename

    # Affichage avec gnuplot
    echo "set terminal png size 600,400 enhanced background rgb 'white'" > gnu_script
    echo "set output 'flag.png'" >> gnu_script
    echo "set title 'Drawing flag of $1" >> gnu_script
    echo "set xr [0:15]" >> gnu_script
    echo "set yr [0:7.5]" >> gnu_script
    echo "unset xtics" >> gnu_script
    echo "unset ytics" >> gnu_script
    echo "set nokey" >> gnu_script
    echo "plot '$filename' with points" >> gnu_script

    gnuplot gnu_script
    
    # Suppresion des fichiers temporaire
    rm gnu_script tmp data.tmp
    
    # Affichage du flag
    display flag.png&
fi
