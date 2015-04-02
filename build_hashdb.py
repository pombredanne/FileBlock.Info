#!/usr/bin/python

import urllib
import os

urlXP = 'http://d0.fileblock.info/XP.7z'
urlVISTA = 'http://d0.fileblock.info/VISTA.7z'
urlWIN2K3 = 'http://d0.fileblock.info/WIN2K3.7z'
urlWIN7 = 'http://d0.fileblock.info/WIN7.7z'
urlWIN2K8 = 'http://d0.fileblock.info/WIN2K8.7z'
urlWIN8 = 'http://d0.fileblock.info/WIN8.7z'
urlWIN2K12 = 'http://d0.fileblock.info/WIN2K12.7z'

print urlXP
if not os.path.isfile('WhiteList-XP.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlXP,'XP.7z')
    print '  uncompressing...'
    os.system('p7zip -d XP.7z')     

print urlVISTA
if not os.path.isfile('WhiteList-VISTA.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVISTA,'VISTA.7z')
    print '  uncompressing...'
    os.system('p7zip -d VISTA.7z')

print urlWIN2K3
if not os.path.isfile('WhiteList-WIN2K3.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlWIN2K3,'WIN2K3.7z')
    print '  uncompressing...'
    os.system('p7zip -d WIN2K3.7z')

print urlWIN7
if not os.path.isfile('WhiteList-WIN7.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlWIN7,'WIN7.7z')
    print '  uncompressing...'
    os.system('p7zip -d WIN7.7z')

print urlWIN2K8
if not os.path.isfile('WhiteList-WIN2K8.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlWIN2K8,'WIN2K8.7z')
    print '  uncompressing...'
    os.system('p7zip -d WIN2K8.7z')

print urlWIN8
if not os.path.isfile('WhiteList-WIN8.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlWIN8,'WIN8.7z')
    print '  uncompressing...'
    os.system('p7zip -d WIN8.7z')

print urlWIN2K12
if not os.path.isfile('WhiteList-WIN2K12.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlWIN2K12,'WIN2K12.7z')
    print '  uncompressing...'
    os.system('p7zip -d WIN2K12.7z')

os.system('hashdb create FileBlock.White')
os.system('hashdb import FileBlock.White WhiteList-XP.DFXML')
os.system('hashdb import FileBlock.White WhiteList-VISTA.DFXML')
os.system('hashdb import FileBlock.White WhiteList-WIN2K3.DFXML')
os.system('hashdb import FileBlock.White WhiteList-WIN7.DFXML')
os.system('hashdb import FileBlock.White WhiteList-WIN2K8.DFXML')
os.system('hashdb import FileBlock.White WhiteList-WIN8.DFXML')
os.system('hashdb import FileBlock.White WhiteList-WIN2K12.DFXML')
os.system('hashdb size FileBlock.White')

urlVxShare000 = 'http://d0.fileblock.info/VxShare000.7z'
urlVxShare001 = 'http://d0.fileblock.info/VxShare001.7z'
urlVxShare002 = 'http://d0.fileblock.info/VxShare002.7z'
urlVxShare003 = 'http://d0.fileblock.info/VxShare003.7z'
urlVxShare004 = 'http://d0.fileblock.info/VxShare004.7z'
urlVxShare005 = 'http://d0.fileblock.info/VxShare005.7z'
urlVxShare006 = 'http://d0.fileblock.info/VxShare006.7z'
urlVxShare007 = 'http://d0.fileblock.info/VxShare007.7z'
urlVxShare008 = 'http://d0.fileblock.info/VxShare008.7z'
urlVxShare009 = 'http://d0.fileblock.info/VxShare009.7z'
urlVxShare010 = 'http://d0.fileblock.info/VxShare010.7z'
urlVxShare011 = 'http://d0.fileblock.info/VxShare011.7z'
urlVxShare012 = 'http://d0.fileblock.info/VxShare012.7z'
urlVxShare013 = 'http://d0.fileblock.info/VxShare013.7z'
urlVxShare014 = 'http://d0.fileblock.info/VxShare014.7z'
urlVxShare015 = 'http://d0.fileblock.info/VxShare015.7z'
urlVxShare016 = 'http://d0.fileblock.info/VxShare016.7z'
urlVxShare017 = 'http://d0.fileblock.info/VxShare017.7z'
urlVxShare018 = 'http://d0.fileblock.info/VxShare018.7z'
urlVxShare019 = 'http://d0.fileblock.info/VxShare019.7z'
urlVxShare020 = 'http://d0.fileblock.info/VxShare020.7z'
urlVxShare021 = 'http://d0.fileblock.info/VxShare021.7z'
urlVxShare022 = 'http://d0.fileblock.info/VxShare022.7z'
urlVxShare023 = 'http://d0.fileblock.info/VxShare023.7z'
urlVxShare024 = 'http://d0.fileblock.info/VxShare024.7z'
urlVxShare025 = 'http://d0.fileblock.info/VxShare025.7z'
urlVxShare026 = 'http://d0.fileblock.info/VxShare026.7z'
urlVxShare027 = 'http://d0.fileblock.info/VxShare027.7z'
urlVxShare028 = 'http://d0.fileblock.info/VxShare028.7z'
urlVxShare029 = 'http://d0.fileblock.info/VxShare029.7z'
urlVxShare030 = 'http://d0.fileblock.info/VxShare030.7z'
urlVxShare031 = 'http://d0.fileblock.info/VxShare031.7z'
urlVxShare032 = 'http://d0.fileblock.info/VxShare032.7z'
urlVxShare033 = 'http://d0.fileblock.info/VxShare033.7z'
urlVxShare034 = 'http://d0.fileblock.info/VxShare034.7z'
urlVxShare035 = 'http://d0.fileblock.info/VxShare035.7z'
urlVxShare036 = 'http://d0.fileblock.info/VxShare036.7z'
urlVxShare037 = 'http://d0.fileblock.info/VxShare037.7z'
urlVxShare038 = 'http://d0.fileblock.info/VxShare038.7z'
urlVxShare039 = 'http://d0.fileblock.info/VxShare039.7z'
urlVxShare040 = 'http://d0.fileblock.info/VxShare040.7z'
urlVxShare041 = 'http://d0.fileblock.info/VxShare041.7z'
urlVxShare042 = 'http://d0.fileblock.info/VxShare042.7z'
urlVxShare043 = 'http://d0.fileblock.info/VxShare043.7z'
urlVxShare044 = 'http://d0.fileblock.info/VxShare044.7z'
urlVxShare045 = 'http://d0.fileblock.info/VxShare045.7z'
urlVxShare046 = 'http://d0.fileblock.info/VxShare046.7z'
urlVxShare047 = 'http://d0.fileblock.info/VxShare047.7z'
urlVxShare048 = 'http://d0.fileblock.info/VxShare048.7z'
urlVxShare049 = 'http://d0.fileblock.info/VxShare049.7z'
urlVxShare050 = 'http://d0.fileblock.info/VxShare050.7z'
urlVxShare051 = 'http://d0.fileblock.info/VxShare051.7z'
urlVxShare052 = 'http://d0.fileblock.info/VxShare052.7z'
urlVxShare053 = 'http://d0.fileblock.info/VxShare053.7z'
urlVxShare054 = 'http://d0.fileblock.info/VxShare054.7z'
urlVxShare055 = 'http://d0.fileblock.info/VxShare055.7z'
urlVxShare056 = 'http://d0.fileblock.info/VxShare056.7z'
urlVxShare057 = 'http://d0.fileblock.info/VxShare057.7z'
urlVxShare058 = 'http://d0.fileblock.info/VxShare058.7z'
urlVxShare059 = 'http://d0.fileblock.info/VxShare059.7z'
urlVxShare060 = 'http://d0.fileblock.info/VxShare060.7z'
urlVxShare061 = 'http://d0.fileblock.info/VxShare061.7z'
urlVxShare062 = 'http://d0.fileblock.info/VxShare062.7z'
urlVxShare063 = 'http://d0.fileblock.info/VxShare063.7z'
urlVxShare064 = 'http://d0.fileblock.info/VxShare064.7z'
urlVxShare065 = 'http://d0.fileblock.info/VxShare065.7z'
urlVxShare066 = 'http://d0.fileblock.info/VxShare066.7z'
urlVxShare067 = 'http://d0.fileblock.info/VxShare067.7z'
urlVxShare068 = 'http://d0.fileblock.info/VxShare068.7z'
urlVxShare069 = 'http://d0.fileblock.info/VxShare069.7z'
urlVxShare070 = 'http://d0.fileblock.info/VxShare070.7z'
urlVxShare071 = 'http://d0.fileblock.info/VxShare071.7z'
urlVxShare072 = 'http://d0.fileblock.info/VxShare072.7z'
urlVxShare073 = 'http://d0.fileblock.info/VxShare073.7z'
urlVxShare074 = 'http://d0.fileblock.info/VxShare074.7z'
urlVxShare075 = 'http://d0.fileblock.info/VxShare075.7z'
urlVxShare076 = 'http://d0.fileblock.info/VxShare076.7z'
urlVxShare077 = 'http://d0.fileblock.info/VxShare077.7z'
urlVxShare078 = 'http://d0.fileblock.info/VxShare078.7z'
urlVxShare079 = 'http://d0.fileblock.info/VxShare079.7z'
urlVxShare080 = 'http://d0.fileblock.info/VxShare080.7z'
urlVxShare081 = 'http://d0.fileblock.info/VxShare081.7z'
urlVxShare082 = 'http://d0.fileblock.info/VxShare082.7z'
urlVxShare083 = 'http://d0.fileblock.info/VxShare083.7z'
urlVxShare084 = 'http://d0.fileblock.info/VxShare084.7z'
urlVxShare085 = 'http://d0.fileblock.info/VxShare085.7z'
urlVxShare086 = 'http://d0.fileblock.info/VxShare086.7z'
urlVxShare087 = 'http://d0.fileblock.info/VxShare087.7z'
urlVxShare088 = 'http://d0.fileblock.info/VxShare088.7z'
urlVxShare089 = 'http://d0.fileblock.info/VxShare089.7z'
urlVxShare090 = 'http://d0.fileblock.info/VxShare090.7z'
urlVxShare091 = 'http://d1.fileblock.info/VxShare091.7z'
urlVxShare092 = 'http://d1.fileblock.info/VxShare092.7z'
urlVxShare093 = 'http://d1.fileblock.info/VxShare093.7z'
urlVxShare094 = 'http://d1.fileblock.info/VxShare094.7z'
urlVxShare095 = 'http://d1.fileblock.info/VxShare095.7z'
urlVxShare096 = 'http://d1.fileblock.info/VxShare096.7z'
urlVxShare097 = 'http://d1.fileblock.info/VxShare097.7z'
urlVxShare098 = 'http://d1.fileblock.info/VxShare098.7z'
urlVxShare099 = 'http://d1.fileblock.info/VxShare099.7z'
urlVxShare100 = 'http://d1.fileblock.info/VxShare100.7z'
urlVxShare101 = 'http://d1.fileblock.info/VxShare101.7z'
urlVxShare102 = 'http://d1.fileblock.info/VxShare102.7z'
urlVxShare103 = 'http://d1.fileblock.info/VxShare103.7z'
urlVxShare104 = 'http://d1.fileblock.info/VxShare104.7z'
urlVxShare105 = 'http://d1.fileblock.info/VxShare105.7z'
urlVxShare106 = 'http://d1.fileblock.info/VxShare106.7z'
urlVxShare107 = 'http://d1.fileblock.info/VxShare107.7z'
urlVxShare108 = 'http://d1.fileblock.info/VxShare108.7z'
urlVxShare109 = 'http://d1.fileblock.info/VxShare109.7z'
urlVxShare110 = 'http://d1.fileblock.info/VxShare110.7z'
urlVxShare111 = 'http://d1.fileblock.info/VxShare111.7z'
urlVxShare112 = 'http://d1.fileblock.info/VxShare112.7z'
urlVxShare113 = 'http://d1.fileblock.info/VxShare113.7z'
urlVxShare114 = 'http://d1.fileblock.info/VxShare114.7z'
urlVxShare115 = 'http://d1.fileblock.info/VxShare115.7z'
urlVxShare116 = 'http://d1.fileblock.info/VxShare116.7z'
urlVxShare117 = 'http://d1.fileblock.info/VxShare117.7z'
urlVxShare118 = 'http://d1.fileblock.info/VxShare118.7z'
urlVxShare119 = 'http://d1.fileblock.info/VxShare119.7z'
urlVxShare120 = 'http://d1.fileblock.info/VxShare120.7z'
urlVxShare121 = 'http://d1.fileblock.info/VxShare121.7z'
urlVxShare122 = 'http://d1.fileblock.info/VxShare122.7z'
urlVxShare123 = 'http://d1.fileblock.info/VxShare123.7z'
urlVxShare124 = 'http://d1.fileblock.info/VxShare124.7z'
urlVxShare125 = 'http://d1.fileblock.info/VxShare125.7z'
urlVxShare126 = 'http://d1.fileblock.info/VxShare126.7z'
urlVxShare127 = 'http://d1.fileblock.info/VxShare127.7z'
urlVxShare128 = 'http://d1.fileblock.info/VxShare128.7z'
urlVxShare129 = 'http://d1.fileblock.info/VxShare129.7z'
urlVxShare130 = 'http://d1.fileblock.info/VxShare130.7z'
urlVxShare131 = 'http://d1.fileblock.info/VxShare131.7z'
urlVxShare132 = 'http://d1.fileblock.info/VxShare132.7z'
urlVxShare133 = 'http://d1.fileblock.info/VxShare133.7z'
urlVxShare134 = 'http://d1.fileblock.info/VxShare134.7z'
urlVxShare135 = 'http://d1.fileblock.info/VxShare135.7z'
urlVxShare136 = 'http://d1.fileblock.info/VxShare136.7z'
urlVxShare137 = 'http://d1.fileblock.info/VxShare137.7z'
urlVxShare138 = 'http://d1.fileblock.info/VxShare138.7z'
urlVxShare139 = 'http://d1.fileblock.info/VxShare139.7z'
urlVxShare140 = 'http://d1.fileblock.info/VxShare140.7z'
urlVxShare141 = 'http://d1.fileblock.info/VxShare141.7z'
urlVxShare142 = 'http://d1.fileblock.info/VxShare142.7z'
urlVxShare143 = 'http://d1.fileblock.info/VxShare143.7z'
urlVxShare144 = 'http://d1.fileblock.info/VxShare144.7z'
urlVxShare145 = 'http://d1.fileblock.info/VxShare145.7z'
urlVxShare146 = 'http://d1.fileblock.info/VxShare146.7z'
urlVxShare147 = 'http://d1.fileblock.info/VxShare147.7z'
urlVxShare148 = 'http://d1.fileblock.info/VxShare148.7z'
urlVxShare149 = 'http://d1.fileblock.info/VxShare149.7z'
urlVxShare150 = 'http://d1.fileblock.info/VxShare150.7z'

print urlVxShare000
if not os.path.isfile('VxShare000.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare000,'VxShare000.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare000.7z')

print urlVxShare001
if not os.path.isfile('VxShare001.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare001,’VxShare001.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare001.7z')

print urlVxShare002
if not os.path.isfile('VxShare002.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare002,’VxShare002.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare002.7z')

print urlVxShare003
if not os.path.isfile('VxShare003.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare003,’VxShare003.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare003.7z')

print urlVxShare004
if not os.path.isfile('VxShare004.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare004,’VxShare004.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare004.7z')

print urlVxShare005
if not os.path.isfile('VxShare005.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare005,’VxShare005.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare005.7z')

print urlVxShare006
if not os.path.isfile('VxShare006.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare006,’VxShare006.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare006.7z')

print urlVxShare007
if not os.path.isfile('VxShare007.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare007,’VxShare007.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare007.7z')

print urlVxShare008
if not os.path.isfile('VxShare008.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare008,’VxShare008.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare008.7z')

print urlVxShare009
if not os.path.isfile('VxShare009.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare009,’VxShare009.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare009.7z')

print urlVxShare010
if not os.path.isfile('VxShare010.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare010,'VxShare010.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare010.7z')

print urlVxShare011
if not os.path.isfile('VxShare011.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare011,’VxShare011.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare011.7z')

print urlVxShare012
if not os.path.isfile('VxShare012.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare012,’VxShare012.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare012.7z')

print urlVxShare013
if not os.path.isfile('VxShare013.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare013,’VxShare013.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare013.7z')

print urlVxShare014
if not os.path.isfile('VxShare014.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare014,’VxShare014.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare014.7z')

print urlVxShare015
if not os.path.isfile('VxShare015.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare015,’VxShare015.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare015.7z')

print urlVxShare016
if not os.path.isfile('VxShare016.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare016,’VxShare016.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare016.7z')

print urlVxShare017
if not os.path.isfile('VxShare017.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare017,’VxShare017.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare017.7z')

print urlVxShare018
if not os.path.isfile('VxShare018.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare018,’VxShare018.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare018.7z')

print urlVxShare019
if not os.path.isfile('VxShare019.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare019,’VxShare019.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare019.7z')

print urlVxShare020
if not os.path.isfile('VxShare020.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare020,'VxShare020.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare020.7z')

print urlVxShare021
if not os.path.isfile('VxShare021.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare021,’VxShare021.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare021.7z')

print urlVxShare022
if not os.path.isfile('VxShare022.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare022,’VxShare022.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare022.7z')

print urlVxShare023
if not os.path.isfile('VxShare023.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare023,’VxShare023.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare023.7z')

print urlVxShare024
if not os.path.isfile('VxShare024.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare024,’VxShare024.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare024.7z')

print urlVxShare025
if not os.path.isfile('VxShare025.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare025,’VxShare025.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare025.7z')

print urlVxShare026
if not os.path.isfile('VxShare026.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare026,’VxShare026.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare026.7z')

print urlVxShare027
if not os.path.isfile('VxShare027.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare027,’VxShare027.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare027.7z')

print urlVxShare028
if not os.path.isfile('VxShare028.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare028,’VxShare028.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare028.7z')

print urlVxShare029
if not os.path.isfile('VxShare029.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare029,’VxShare029.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare029.7z')

print urlVxShare030
if not os.path.isfile('VxShare030.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare030,'VxShare030.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare030.7z')

print urlVxShare031
if not os.path.isfile('VxShare031.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare031,’VxShare031.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare031.7z')

print urlVxShare032
if not os.path.isfile('VxShare032.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare032,’VxShare032.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare032.7z')

print urlVxShare033
if not os.path.isfile('VxShare033.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare033,’VxShare033.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare033.7z')

print urlVxShare034
if not os.path.isfile('VxShare034.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare034,’VxShare034.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare034.7z')

print urlVxShare035
if not os.path.isfile('VxShare035.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare035,’VxShare035.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare035.7z')

print urlVxShare036
if not os.path.isfile('VxShare036.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare036,’VxShare036.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare036.7z')

print urlVxShare037
if not os.path.isfile('VxShare037.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare037,’VxShare037.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare037.7z')

print urlVxShare038
if not os.path.isfile('VxShare038.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare038,’VxShare038.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare038.7z')

print urlVxShare039
if not os.path.isfile('VxShare039.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare039,’VxShare039.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare039.7z')

print urlVxShare040
if not os.path.isfile('VxShare040.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare040,'VxShare040.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare040.7z')

print urlVxShare041
if not os.path.isfile('VxShare041.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare041,’VxShare041.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare041.7z')

print urlVxShare042
if not os.path.isfile('VxShare042.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare042,’VxShare042.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare042.7z')

print urlVxShare043
if not os.path.isfile('VxShare043.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare043,’VxShare043.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare043.7z')

print urlVxShare044
if not os.path.isfile('VxShare044.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare044,’VxShare044.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare044.7z')

print urlVxShare045
if not os.path.isfile('VxShare045.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare045,’VxShare045.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare045.7z')

print urlVxShare046
if not os.path.isfile('VxShare046.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare046,’VxShare046.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare046.7z')

print urlVxShare047
if not os.path.isfile('VxShare047.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare047,’VxShare047.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare047.7z')

print urlVxShare048
if not os.path.isfile('VxShare048.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare048,’VxShare048.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare048.7z')

print urlVxShare049
if not os.path.isfile('VxShare049.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare049,’VxShare049.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare049.7z')

print urlVxShare050
if not os.path.isfile('VxShare050.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare050,'VxShare050.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare050.7z')

print urlVxShare051
if not os.path.isfile('VxShare051.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare051,’VxShare051.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare051.7z')

print urlVxShare052
if not os.path.isfile('VxShare052.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare052,’VxShare052.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare052.7z')

print urlVxShare053
if not os.path.isfile('VxShare053.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare053,’VxShare053.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare053.7z')

print urlVxShare054
if not os.path.isfile('VxShare054.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare054,’VxShare054.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare054.7z')

print urlVxShare055
if not os.path.isfile('VxShare055.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare055,’VxShare055.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare055.7z')

print urlVxShare056
if not os.path.isfile('VxShare056.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare056,’VxShare056.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare056.7z')

print urlVxShare057
if not os.path.isfile('VxShare057.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare057,’VxShare057.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare057.7z')

print urlVxShare058
if not os.path.isfile('VxShare058.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare058,’VxShare058.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare058.7z')

print urlVxShare059
if not os.path.isfile('VxShare059.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare059,’VxShare059.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare059.7z')

print urlVxShare060
if not os.path.isfile('VxShare060.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare060,’VxShare060.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare060.7z')

print urlVxShare061
if not os.path.isfile('VxShare061.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare061,’VxShare061.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare061.7z')

print urlVxShare062
if not os.path.isfile('VxShare062.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare062,’VxShare062.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare062.7z')

print urlVxShare063
if not os.path.isfile('VxShare063.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare063,’VxShare063.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare063.7z')

print urlVxShare064
if not os.path.isfile('VxShare064.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare064,’VxShare064.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare064.7z')

print urlVxShare065
if not os.path.isfile('VxShare065.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare065,’VxShare065.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare065.7z')

print urlVxShare066
if not os.path.isfile('VxShare066.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare066,’VxShare066.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare066.7z')

print urlVxShare067
if not os.path.isfile('VxShare067.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare067,’VxShare067.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare067.7z')

print urlVxShare068
if not os.path.isfile('VxShare068.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare068,’VxShare068.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare068.7z')

print urlVxShare069
if not os.path.isfile('VxShare069.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare069,’VxShare069.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare069.7z')

print urlVxShare070
if not os.path.isfile('VxShare070.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare070,'VxShare070.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare070.7z')

print urlVxShare071
if not os.path.isfile('VxShare071.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare071,’VxShare071.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare071.7z')

print urlVxShare072
if not os.path.isfile('VxShare072.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare072,’VxShare072.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare072.7z')

print urlVxShare073
if not os.path.isfile('VxShare073.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare073,’VxShare073.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare073.7z')

print urlVxShare074
if not os.path.isfile('VxShare074.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare074,’VxShare074.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare074.7z')

print urlVxShare075
if not os.path.isfile('VxShare075.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare075,’VxShare075.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare075.7z')

print urlVxShare076
if not os.path.isfile('VxShare076.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare076,’VxShare076.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare076.7z')

print urlVxShare077
if not os.path.isfile('VxShare077.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare077,’VxShare077.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare077.7z')

print urlVxShare078
if not os.path.isfile('VxShare078.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare078,’VxShare078.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare078.7z')

print urlVxShare079
if not os.path.isfile('VxShare079.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare079,’VxShare079.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare079.7z')

print urlVxShare080
if not os.path.isfile('VxShare080.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare080,'VxShare080.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare080.7z')

print urlVxShare081
if not os.path.isfile('VxShare081.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare081,’VxShare081.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare081.7z')

print urlVxShare082
if not os.path.isfile('VxShare082.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare082,’VxShare082.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare082.7z')

print urlVxShare083
if not os.path.isfile('VxShare083.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare083,’VxShare083.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare083.7z')

print urlVxShare084
if not os.path.isfile('VxShare084.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare084,’VxShare084.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare084.7z')

print urlVxShare085
if not os.path.isfile('VxShare085.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare085,’VxShare085.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare085.7z')

print urlVxShare086
if not os.path.isfile('VxShare086.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare086,’VxShare086.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare086.7z')

print urlVxShare087
if not os.path.isfile('VxShare087.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare087,’VxShare087.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare087.7z')

print urlVxShare088
if not os.path.isfile('VxShare088.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare088,’VxShare088.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare088.7z')

print urlVxShare089
if not os.path.isfile('VxShare089.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare089,’VxShare089.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare089.7z')

print urlVxShare090
if not os.path.isfile('VxShare090.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare090,'VxShare090.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare090.7z')

print urlVxShare100
if not os.path.isfile('VxShare100.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare100,'VxShare100.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare100.7z')

print urlVxShare101
if not os.path.isfile('VxShare101.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare101,’VxShare101.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare101.7z')

print urlVxShare102
if not os.path.isfile('VxShare102.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare102,’VxShare102.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare102.7z')

print urlVxShare103
if not os.path.isfile('VxShare103.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare103,’VxShare103.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare103.7z')

print urlVxShare104
if not os.path.isfile('VxShare104.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare104,’VxShare104.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare104.7z')

print urlVxShare105
if not os.path.isfile('VxShare105.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare105,’VxShare105.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare105.7z')

print urlVxShare106
if not os.path.isfile('VxShare106.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare106,’VxShare106.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare106.7z')

print urlVxShare107
if not os.path.isfile('VxShare107.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare107,’VxShare107.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare107.7z')

print urlVxShare108
if not os.path.isfile('VxShare108.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare108,’VxShare108.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare108.7z')

print urlVxShare109
if not os.path.isfile('VxShare109.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare109,’VxShare109.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare109.7z')

print urlVxShare110
if not os.path.isfile('VxShare110.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare110,’VxShare110.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare110.7z')

print urlVxShare111
if not os.path.isfile('VxShare111.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare111,’VxShare111.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare111.7z')

print urlVxShare112
if not os.path.isfile('VxShare112.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare112,’VxShare112.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare112.7z')

print urlVxShare113
if not os.path.isfile('VxShare113.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare113,’VxShare113.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare113.7z')

print urlVxShare114
if not os.path.isfile('VxShare114.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare114,’VxShare114.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare114.7z')

print urlVxShare115
if not os.path.isfile('VxShare115.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare115,’VxShare115.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare115.7z')

print urlVxShare116
if not os.path.isfile('VxShare116.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare116,’VxShare116.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare116.7z')

print urlVxShare117
if not os.path.isfile('VxShare117.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare117,’VxShare117.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare117.7z')

print urlVxShare118
if not os.path.isfile('VxShare118.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare118,’VxShare118.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare118.7z')

print urlVxShare119
if not os.path.isfile('VxShare119.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare119,’VxShare119.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare119.7z')

print urlVxShare120
if not os.path.isfile('VxShare120.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare120,’VxShare120.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare120.7z')

print urlVxShare121
if not os.path.isfile('VxShare121.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare121,’VxShare121.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare121.7z')

print urlVxShare122
if not os.path.isfile('VxShare122.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare122,’VxShare122.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare122.7z')

print urlVxShare123
if not os.path.isfile('VxShare123.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare123,’VxShare123.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare123.7z')

print urlVxShare124
if not os.path.isfile('VxShare124.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare124,’VxShare124.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare124.7z')

print urlVxShare125
if not os.path.isfile('VxShare125.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare125,’VxShare125.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare125.7z')

print urlVxShare0126
if not os.path.isfile('VxShare0126.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare0126,’VxShare0126.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare0126.7z')

print urlVxShare127
if not os.path.isfile('VxShare127.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare127,’VxShare127.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare127.7z')

print urlVxShare128
if not os.path.isfile('VxShare128.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare128,’VxShare128.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare128.7z')

print urlVxShare129
if not os.path.isfile('VxShare129.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare129,’VxShare129.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare129.7z')

print urlVxShare130
if not os.path.isfile('VxShare130.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare130,’VxShare130.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare130.7z')

print urlVxShare131
if not os.path.isfile('VxShare131.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare131,’VxShare131.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare131.7z')

print urlVxShare132
if not os.path.isfile('VxShare132.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare132,’VxShare132.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare132.7z')

print urlVxShare133
if not os.path.isfile('VxShare133.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare133,’VxShare133.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare133.7z')

print urlVxShare134
if not os.path.isfile('VxShare134.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare134,’VxShare134.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare134.7z')

print urlVxShare135
if not os.path.isfile('VxShare135.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare135,’VxShare135.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare135.7z')

print urlVxShare136
if not os.path.isfile('VxShare136.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare136,’VxShare136.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare136.7z')

print urlVxShare137
if not os.path.isfile('VxShare137.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare137,’VxShare137.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare137.7z')

print urlVxShare138
if not os.path.isfile('VxShare138.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare138,’VxShare138.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare138.7z')

print urlVxShare139
if not os.path.isfile('VxShare139.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare139,’VxShare139.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare139.7z')

print urlVxShare140
if not os.path.isfile('VxShare140.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare140,’VxShare140.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare140.7z')

print urlVxShare141
if not os.path.isfile('VxShare141.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare141,’VxShare141.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare141.7z')

print urlVxShare142
if not os.path.isfile('VxShare142.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare142,’VxShare142.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare142.7z')

print urlVxShare143
if not os.path.isfile('VxShare143.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare143,’VxShare143.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare143.7z')

print urlVxShare144
if not os.path.isfile('VxShare144.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare144,’VxShare144.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare144.7z')

print urlVxShare145
if not os.path.isfile('VxShare145.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare145,’VxShare145.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare145.7z')

print urlVxShare146
if not os.path.isfile('VxShare146.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare146,’VxShare146.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare146.7z')

print urlVxShare147
if not os.path.isfile('VxShare147.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare147,’VxShare147.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare147.7z')

print urlVxShare148
if not os.path.isfile('VxShare148-DFXML.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare148,’VxShare148.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare148.7z')

print urlVxShare149
if not os.path.isfile('VxShare149-DFXML.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare149,’VxShare149.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare149.7z')

print urlVxShare150
if not os.path.isfile('VxShare150.DFXML'):
    print '  downloading...'
    urllib.urlretrieve(urlVxShare150,’VxShare150.7z')
    print '  uncompressing...'
    os.system('p7zip -d VxShare150.7z')

os.system('hashdb create FileBlock.Import')
os.system('hashdb import FileBlock.Import VxShare000.DFXML')
os.system('hashdb import FileBlock.Import VxShare001.DFXML')
os.system('hashdb import FileBlock.Import VxShare002.DFXML')
os.system('hashdb import FileBlock.Import VxShare003.DFXML')
os.system('hashdb import FileBlock.Import VxShare004.DFXML')
os.system('hashdb import FileBlock.Import VxShare005.DFXML')
os.system('hashdb import FileBlock.Import VxShare006.DFXML')
os.system('hashdb import FileBlock.Import VxShare007.DFXML')
os.system('hashdb import FileBlock.Import VxShare008.DFXML')
os.system('hashdb import FileBlock.Import VxShare009.DFXML')
os.system('hashdb import FileBlock.Import VxShare010.DFXML')
os.system('hashdb import FileBlock.Import VxShare011.DFXML')
os.system('hashdb import FileBlock.Import VxShare012.DFXML')
os.system('hashdb import FileBlock.Import VxShare013.DFXML')
os.system('hashdb import FileBlock.Import VxShare014.DFXML')
os.system('hashdb import FileBlock.Import VxShare015.DFXML')
os.system('hashdb import FileBlock.Import VxShare016.DFXML')
os.system('hashdb import FileBlock.Import VxShare017.DFXML')
os.system('hashdb import FileBlock.Import VxShare018.DFXML')
os.system('hashdb import FileBlock.Import VxShare019.DFXML')
os.system('hashdb import FileBlock.Import VxShare020.DFXML')
os.system('hashdb import FileBlock.Import VxShare021.DFXML')
os.system('hashdb import FileBlock.Import VxShare022.DFXML')
os.system('hashdb import FileBlock.Import VxShare023.DFXML')
os.system('hashdb import FileBlock.Import VxShare024.DFXML')
os.system('hashdb import FileBlock.Import VxShare025.DFXML')
os.system('hashdb import FileBlock.Import VxShare026.DFXML')
os.system('hashdb import FileBlock.Import VxShare027.DFXML')
os.system('hashdb import FileBlock.Import VxShare028.DFXML')
os.system('hashdb import FileBlock.Import VxShare029.DFXML')
os.system('hashdb import FileBlock.Import VxShare030.DFXML')
os.system('hashdb import FileBlock.Import VxShare031.DFXML')
os.system('hashdb import FileBlock.Import VxShare032.DFXML')
os.system('hashdb import FileBlock.Import VxShare033.DFXML')
os.system('hashdb import FileBlock.Import VxShare034.DFXML')
os.system('hashdb import FileBlock.Import VxShare035.DFXML')
os.system('hashdb import FileBlock.Import VxShare036.DFXML')
os.system('hashdb import FileBlock.Import VxShare037.DFXML')
os.system('hashdb import FileBlock.Import VxShare038.DFXML')
os.system('hashdb import FileBlock.Import VxShare039.DFXML')
os.system('hashdb import FileBlock.Import VxShare040.DFXML')
os.system('hashdb import FileBlock.Import VxShare041.DFXML')
os.system('hashdb import FileBlock.Import VxShare042.DFXML')
os.system('hashdb import FileBlock.Import VxShare043.DFXML')
os.system('hashdb import FileBlock.Import VxShare044.DFXML')
os.system('hashdb import FileBlock.Import VxShare045.DFXML')
os.system('hashdb import FileBlock.Import VxShare046.DFXML')
os.system('hashdb import FileBlock.Import VxShare047.DFXML')
os.system('hashdb import FileBlock.Import VxShare048.DFXML')
os.system('hashdb import FileBlock.Import VxShare049.DFXML')
os.system('hashdb import FileBlock.Import VxShare050.DFXML')
os.system('hashdb import FileBlock.Import VxShare051.DFXML')
os.system('hashdb import FileBlock.Import VxShare052.DFXML')
os.system('hashdb import FileBlock.Import VxShare053.DFXML')
os.system('hashdb import FileBlock.Import VxShare054.DFXML')
os.system('hashdb import FileBlock.Import VxShare055.DFXML')
os.system('hashdb import FileBlock.Import VxShare056.DFXML')
os.system('hashdb import FileBlock.Import VxShare057.DFXML')
os.system('hashdb import FileBlock.Import VxShare058.DFXML')
os.system('hashdb import FileBlock.Import VxShare059.DFXML')
os.system('hashdb import FileBlock.Import VxShare060.DFXML')
os.system('hashdb import FileBlock.Import VxShare061.DFXML')
os.system('hashdb import FileBlock.Import VxShare062.DFXML')
os.system('hashdb import FileBlock.Import VxShare063.DFXML')
os.system('hashdb import FileBlock.Import VxShare064.DFXML')
os.system('hashdb import FileBlock.Import VxShare065.DFXML')
os.system('hashdb import FileBlock.Import VxShare066.DFXML')
os.system('hashdb import FileBlock.Import VxShare067.DFXML')
os.system('hashdb import FileBlock.Import VxShare068.DFXML')
os.system('hashdb import FileBlock.Import VxShare069.DFXML')
os.system('hashdb import FileBlock.Import VxShare070.DFXML')
os.system('hashdb import FileBlock.Import VxShare071.DFXML')
os.system('hashdb import FileBlock.Import VxShare072.DFXML')
os.system('hashdb import FileBlock.Import VxShare073.DFXML')
os.system('hashdb import FileBlock.Import VxShare074.DFXML')
os.system('hashdb import FileBlock.Import VxShare075.DFXML')
os.system('hashdb import FileBlock.Import VxShare076.DFXML')
os.system('hashdb import FileBlock.Import VxShare077.DFXML')
os.system('hashdb import FileBlock.Import VxShare078.DFXML')
os.system('hashdb import FileBlock.Import VxShare079.DFXML')
os.system('hashdb import FileBlock.Import VxShare080.DFXML')
os.system('hashdb import FileBlock.Import VxShare081.DFXML')
os.system('hashdb import FileBlock.Import VxShare082.DFXML')
os.system('hashdb import FileBlock.Import VxShare083.DFXML')
os.system('hashdb import FileBlock.Import VxShare084.DFXML')
os.system('hashdb import FileBlock.Import VxShare085.DFXML')
os.system('hashdb import FileBlock.Import VxShare086.DFXML')
os.system('hashdb import FileBlock.Import VxShare087.DFXML')
os.system('hashdb import FileBlock.Import VxShare088.DFXML')
os.system('hashdb import FileBlock.Import VxShare089.DFXML')
os.system('hashdb import FileBlock.Import VxShare090.DFXML')
os.system('hashdb import FileBlock.Import VxShare091.DFXML')
os.system('hashdb import FileBlock.Import VxShare092.DFXML')
os.system('hashdb import FileBlock.Import VxShare093.DFXML')
os.system('hashdb import FileBlock.Import VxShare094.DFXML')
os.system('hashdb import FileBlock.Import VxShare095.DFXML')
os.system('hashdb import FileBlock.Import VxShare096.DFXML')
os.system('hashdb import FileBlock.Import VxShare097.DFXML')
os.system('hashdb import FileBlock.Import VxShare098.DFXML')
os.system('hashdb import FileBlock.Import VxShare099.DFXML')
os.system('hashdb import FileBlock.Import VxShare100.DFXML')
os.system('hashdb import FileBlock.Import VxShare101.DFXML')
os.system('hashdb import FileBlock.Import VxShare102.DFXML')
os.system('hashdb import FileBlock.Import VxShare103.DFXML')
os.system('hashdb import FileBlock.Import VxShare104.DFXML')
os.system('hashdb import FileBlock.Import VxShare105.DFXML')
os.system('hashdb import FileBlock.Import VxShare106.DFXML')
os.system('hashdb import FileBlock.Import VxShare107.DFXML')
os.system('hashdb import FileBlock.Import VxShare108.DFXML')
os.system('hashdb import FileBlock.Import VxShare109.DFXML')
os.system('hashdb import FileBlock.Import VxShare110.DFXML')
os.system('hashdb import FileBlock.Import VxShare111.DFXML')
os.system('hashdb import FileBlock.Import VxShare112.DFXML')
os.system('hashdb import FileBlock.Import VxShare113.DFXML')
os.system('hashdb import FileBlock.Import VxShare114.DFXML')
os.system('hashdb import FileBlock.Import VxShare115.DFXML')
os.system('hashdb import FileBlock.Import VxShare116.DFXML')
os.system('hashdb import FileBlock.Import VxShare117.DFXML')
os.system('hashdb import FileBlock.Import VxShare118.DFXML')
os.system('hashdb import FileBlock.Import VxShare119.DFXML')
os.system('hashdb import FileBlock.Import VxShare120.DFXML')
os.system('hashdb import FileBlock.Import VxShare121.DFXML')
os.system('hashdb import FileBlock.Import VxShare122.DFXML')
os.system('hashdb import FileBlock.Import VxShare123.DFXML')
os.system('hashdb import FileBlock.Import VxShare124.DFXML')
os.system('hashdb import FileBlock.Import VxShare125.DFXML')
os.system('hashdb import FileBlock.Import VxShare126.DFXML')
os.system('hashdb import FileBlock.Import VxShare127.DFXML')
os.system('hashdb import FileBlock.Import VxShare128.DFXML')
os.system('hashdb import FileBlock.Import VxShare129.DFXML')
os.system('hashdb import FileBlock.Import VxShare130.DFXML')
os.system('hashdb import FileBlock.Import VxShare131.DFXML')
os.system('hashdb import FileBlock.Import VxShare132.DFXML')
os.system('hashdb import FileBlock.Import VxShare133.DFXML')
os.system('hashdb import FileBlock.Import VxShare134.DFXML')
os.system('hashdb import FileBlock.Import VxShare135.DFXML')
os.system('hashdb import FileBlock.Import VxShare136.DFXML')
os.system('hashdb import FileBlock.Import VxShare137.DFXML')
os.system('hashdb import FileBlock.Import VxShare138.DFXML')
os.system('hashdb import FileBlock.Import VxShare139.DFXML')
os.system('hashdb import FileBlock.Import VxShare140.DFXML')
os.system('hashdb import FileBlock.Import VxShare141.DFXML')
os.system('hashdb import FileBlock.Import VxShare142.DFXML')
os.system('hashdb import FileBlock.Import VxShare143.DFXML')
os.system('hashdb import FileBlock.Import VxShare144.DFXML')
os.system('hashdb import FileBlock.Import VxShare145.DFXML')
os.system('hashdb import FileBlock.Import VxShare146.DFXML')
os.system('hashdb import FileBlock.Import VxShare147.DFXML')
os.system('hashdb import FileBlock.Import VxShare148-DFXML.DFXML')
os.system('hashdb import FileBlock.Import VxShare149-DFXML.DFXML')
os.system('hashdb import FileBlock.Import VxShare150.DFXML')
os.system('hashdb size FileBlock.Import')

os.system('hashdb create FileBlock.Info’)
os.system('hashdb subtract FileBlock.Import FileBlock.White FileBlock.Info')
os.system('hashdb size FileBlock.Info')
