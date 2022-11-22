#!/bin/bash 

resultado=$(find /tmp/ -name "*.txt" -type f 2>/dev/null) 
echo $resultado

rm -rf $resultado