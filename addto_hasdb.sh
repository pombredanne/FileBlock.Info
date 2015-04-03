#!/bin/bash

wget http://d1.fileblock.info/VxShare150.7z
p7zip -d VxShare150.7z
hashdb create VxShare150
hashdb import VxShare150 VxShare150.dfxml
hashdb create VxShare150_TEMP
hashdb subtract VxShare150 FileBlock.White VxShare150_TEMP
hashdb add VxShare150_TEMP FileBlock.Info
