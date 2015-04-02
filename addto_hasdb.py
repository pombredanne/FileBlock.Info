#!/usr/bin/python

import os

name = 'VxShare150'

url = 'wget http://d1.fileblock.info/'+name+'.7z'
file = 'p7zip -d '+ name+'.7z'
dfxml = name+'.dfxml'
create = 'hashdb create '+name
input = 'hashdb import '+name+' '+dfxml
temp = 'hashdb create '+name+'_temp'
white = 'hashdb subtract '+name+' FileBlock.White '+name+'_temp'
add = 'hashdb add '+name+'_temp FileBlock.Info'

os.system(url)
os.system(file)     
os.system(create)
os.system(input)
os.system(temp)
os.system(white)
os.system(add)
