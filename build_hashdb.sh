#!/bin/bash


sudo apt-get -y install p7zip

wget http://d0.fileblock.info/XP.7z
wget http://d0.fileblock.info/VISTA.7z
wget http://d0.fileblock.info/WIN2K3.7z
wget http://d0.fileblock.info/WIN7.7z
wget http://d0.fileblock.info/WIN2K8.7z
wget http://d0.fileblock.info/WIN8.7z
wget http://d0.fileblock.info/WIN2K12.7z

p7zip -d XP.7z 
p7zip -d VISTA.7z
p7zip -d WIN2K3.7z
p7zip -d WIN7.7z
p7zip -d WIN2K8.7z
p7zip -d WIN8.7z
p7zip -d WIN2K12.7z

hashdb create FileBlock.White
hashdb import FileBlock.White WhiteList-XP.DFXML
hashdb import FileBlock.White WhiteList-VISTA.DFXML
hashdb import FileBlock.White WhiteList-WIN2K3.DFXML
hashdb import FileBlock.White WhiteList-WIN7.DFXML
hashdb import FileBlock.White WhiteList-WIN2K8.DFXML
hashdb import FileBlock.White WhiteList-WIN8.DFXML
hashdb import FileBlock.White WhiteList-WIN2K12.DFXML
hashdb size FileBlock.White

wget http://d0.fileblock.info/VxShare000.7z
wget http://d0.fileblock.info/VxShare001.7z
wget http://d0.fileblock.info/VxShare002.7z
wget http://d0.fileblock.info/VxShare003.7z
wget http://d0.fileblock.info/VxShare004.7z
wget http://d0.fileblock.info/VxShare005.7z
wget http://d0.fileblock.info/VxShare006.7z
wget http://d0.fileblock.info/VxShare007.7z
wget http://d0.fileblock.info/VxShare008.7z
wget http://d0.fileblock.info/VxShare009.7z
wget http://d0.fileblock.info/VxShare010.7z
wget http://d0.fileblock.info/VxShare011.7z
wget http://d0.fileblock.info/VxShare012.7z
wget http://d0.fileblock.info/VxShare013.7z
wget http://d0.fileblock.info/VxShare014.7z
wget http://d0.fileblock.info/VxShare015.7z
wget http://d0.fileblock.info/VxShare016.7z
wget http://d0.fileblock.info/VxShare017.7z
wget http://d0.fileblock.info/VxShare018.7z
wget http://d0.fileblock.info/VxShare019.7z
wget http://d0.fileblock.info/VxShare020.7z
wget http://d0.fileblock.info/VxShare021.7z
wget http://d0.fileblock.info/VxShare022.7z
wget http://d0.fileblock.info/VxShare023.7z
wget http://d0.fileblock.info/VxShare024.7z
wget http://d0.fileblock.info/VxShare025.7z
wget http://d0.fileblock.info/VxShare026.7z
wget http://d0.fileblock.info/VxShare027.7z
wget http://d0.fileblock.info/VxShare028.7z
wget http://d0.fileblock.info/VxShare029.7z
wget http://d0.fileblock.info/VxShare030.7z
wget http://d0.fileblock.info/VxShare031.7z
wget http://d0.fileblock.info/VxShare032.7z
wget http://d0.fileblock.info/VxShare033.7z
wget http://d0.fileblock.info/VxShare034.7z
wget http://d0.fileblock.info/VxShare035.7z
wget http://d0.fileblock.info/VxShare036.7z
wget http://d0.fileblock.info/VxShare037.7z
wget http://d0.fileblock.info/VxShare038.7z
wget http://d0.fileblock.info/VxShare039.7z
wget http://d0.fileblock.info/VxShare040.7z
wget http://d0.fileblock.info/VxShare041.7z
wget http://d0.fileblock.info/VxShare042.7z
wget http://d0.fileblock.info/VxShare043.7z
wget http://d0.fileblock.info/VxShare044.7z
wget http://d0.fileblock.info/VxShare045.7z
wget http://d0.fileblock.info/VxShare046.7z
wget http://d0.fileblock.info/VxShare047.7z
wget http://d0.fileblock.info/VxShare048.7z
wget http://d0.fileblock.info/VxShare049.7z
wget http://d0.fileblock.info/VxShare050.7z
wget http://d0.fileblock.info/VxShare051.7z
wget http://d0.fileblock.info/VxShare052.7z
wget http://d0.fileblock.info/VxShare053.7z
wget http://d0.fileblock.info/VxShare054.7z
wget http://d0.fileblock.info/VxShare055.7z
wget http://d0.fileblock.info/VxShare056.7z
wget http://d0.fileblock.info/VxShare057.7z
wget http://d0.fileblock.info/VxShare058.7z
wget http://d0.fileblock.info/VxShare059.7z
wget http://d0.fileblock.info/VxShare060.7z
wget http://d0.fileblock.info/VxShare061.7z
wget http://d0.fileblock.info/VxShare062.7z
wget http://d0.fileblock.info/VxShare063.7z
wget http://d0.fileblock.info/VxShare064.7z
wget http://d0.fileblock.info/VxShare065.7z
wget http://d0.fileblock.info/VxShare066.7z
wget http://d0.fileblock.info/VxShare067.7z
wget http://d0.fileblock.info/VxShare068.7z
wget http://d0.fileblock.info/VxShare069.7z
wget http://d0.fileblock.info/VxShare070.7z
wget http://d0.fileblock.info/VxShare071.7z
wget http://d0.fileblock.info/VxShare072.7z
wget http://d0.fileblock.info/VxShare073.7z
wget http://d0.fileblock.info/VxShare074.7z
wget http://d0.fileblock.info/VxShare075.7z
wget http://d0.fileblock.info/VxShare076.7z
wget http://d0.fileblock.info/VxShare077.7z
wget http://d0.fileblock.info/VxShare078.7z
wget http://d0.fileblock.info/VxShare079.7z
wget http://d0.fileblock.info/VxShare080.7z
wget http://d0.fileblock.info/VxShare081.7z
wget http://d0.fileblock.info/VxShare082.7z
wget http://d0.fileblock.info/VxShare083.7z
wget http://d0.fileblock.info/VxShare084.7z
wget http://d0.fileblock.info/VxShare085.7z
wget http://d0.fileblock.info/VxShare086.7z
wget http://d0.fileblock.info/VxShare087.7z
wget http://d0.fileblock.info/VxShare088.7z
wget http://d0.fileblock.info/VxShare089.7z
wget http://d0.fileblock.info/VxShare090.7z
wget http://d1.fileblock.info/VxShare091.7z
wget http://d1.fileblock.info/VxShare092.7z
wget http://d1.fileblock.info/VxShare093.7z
wget http://d1.fileblock.info/VxShare094.7z
wget http://d1.fileblock.info/VxShare095.7z
wget http://d1.fileblock.info/VxShare096.7z
wget http://d1.fileblock.info/VxShare097.7z
wget http://d1.fileblock.info/VxShare098.7z
wget http://d1.fileblock.info/VxShare099.7z
wget http://d1.fileblock.info/VxShare100.7z
wget http://d1.fileblock.info/VxShare101.7z
wget http://d1.fileblock.info/VxShare102.7z
wget http://d1.fileblock.info/VxShare103.7z
wget http://d1.fileblock.info/VxShare104.7z
wget http://d1.fileblock.info/VxShare105.7z
wget http://d1.fileblock.info/VxShare106.7z
wget http://d1.fileblock.info/VxShare107.7z
wget http://d1.fileblock.info/VxShare108.7z
wget http://d1.fileblock.info/VxShare109.7z
wget http://d1.fileblock.info/VxShare110.7z
wget http://d1.fileblock.info/VxShare111.7z
wget http://d1.fileblock.info/VxShare112.7z
wget http://d1.fileblock.info/VxShare113.7z
wget http://d1.fileblock.info/VxShare114.7z
wget http://d1.fileblock.info/VxShare115.7z
wget http://d1.fileblock.info/VxShare116.7z
wget http://d1.fileblock.info/VxShare117.7z
wget http://d1.fileblock.info/VxShare118.7z
wget http://d1.fileblock.info/VxShare119.7z
wget http://d1.fileblock.info/VxShare120.7z
wget http://d1.fileblock.info/VxShare121.7z
wget http://d1.fileblock.info/VxShare122.7z
wget http://d1.fileblock.info/VxShare123.7z
wget http://d1.fileblock.info/VxShare124.7z
wget http://d1.fileblock.info/VxShare125.7z
wget http://d1.fileblock.info/VxShare126.7z
wget http://d1.fileblock.info/VxShare127.7z
wget http://d1.fileblock.info/VxShare128.7z
wget http://d1.fileblock.info/VxShare129.7z
wget http://d1.fileblock.info/VxShare130.7z
wget http://d1.fileblock.info/VxShare131.7z
wget http://d1.fileblock.info/VxShare132.7z
wget http://d1.fileblock.info/VxShare133.7z
wget http://d1.fileblock.info/VxShare134.7z
wget http://d1.fileblock.info/VxShare135.7z
wget http://d1.fileblock.info/VxShare136.7z
wget http://d1.fileblock.info/VxShare137.7z
wget http://d1.fileblock.info/VxShare138.7z
wget http://d1.fileblock.info/VxShare139.7z
wget http://d1.fileblock.info/VxShare140.7z
wget http://d1.fileblock.info/VxShare141.7z
wget http://d1.fileblock.info/VxShare142.7z
wget http://d1.fileblock.info/VxShare143.7z
wget http://d1.fileblock.info/VxShare144.7z
wget http://d1.fileblock.info/VxShare145.7z
wget http://d1.fileblock.info/VxShare146.7z
wget http://d1.fileblock.info/VxShare147.7z
wget http://d1.fileblock.info/VxShare148.7z
wget http://d1.fileblock.info/VxShare149.7z
wget http://d1.fileblock.info/VxShare150.7z

p7zip -d VxShare000.7z
p7zip -d VxShare001.7z
p7zip -d VxShare002.7z
p7zip -d VxShare003.7z
p7zip -d VxShare004.7z
p7zip -d VxShare005.7z
p7zip -d VxShare006.7z
p7zip -d VxShare007.7z
p7zip -d VxShare008.7z
p7zip -d VxShare009.7z
p7zip -d VxShare010.7z
p7zip -d VxShare011.7z
p7zip -d VxShare012.7z
p7zip -d VxShare013.7z
p7zip -d VxShare014.7z
p7zip -d VxShare015.7z
p7zip -d VxShare016.7z
p7zip -d VxShare017.7z
p7zip -d VxShare018.7z
p7zip -d VxShare019.7z
p7zip -d VxShare020.7z
p7zip -d VxShare021.7z
p7zip -d VxShare022.7z
p7zip -d VxShare023.7z
p7zip -d VxShare024.7z
p7zip -d VxShare025.7z
p7zip -d VxShare026.7z
p7zip -d VxShare027.7z
p7zip -d VxShare028.7z
p7zip -d VxShare029.7z
p7zip -d VxShare030.7z
p7zip -d VxShare031.7z
p7zip -d VxShare032.7z
p7zip -d VxShare033.7z
p7zip -d VxShare034.7z
p7zip -d VxShare035.7z
p7zip -d VxShare036.7z
p7zip -d VxShare037.7z
p7zip -d VxShare038.7z
p7zip -d VxShare039.7z
p7zip -d VxShare040.7z
p7zip -d VxShare041.7z
p7zip -d VxShare042.7z
p7zip -d VxShare043.7z
p7zip -d VxShare044.7z
p7zip -d VxShare045.7z
p7zip -d VxShare046.7z
p7zip -d VxShare047.7z
p7zip -d VxShare048.7z
p7zip -d VxShare049.7z
p7zip -d VxShare050.7z
p7zip -d VxShare051.7z
p7zip -d VxShare052.7z
p7zip -d VxShare053.7z
p7zip -d VxShare054.7z
p7zip -d VxShare055.7z
p7zip -d VxShare056.7z
p7zip -d VxShare057.7z
p7zip -d VxShare058.7z
p7zip -d VxShare059.7z
p7zip -d VxShare060.7z
p7zip -d VxShare061.7z
p7zip -d VxShare062.7z
p7zip -d VxShare063.7z
p7zip -d VxShare064.7z
p7zip -d VxShare065.7z
p7zip -d VxShare066.7z
p7zip -d VxShare067.7z
p7zip -d VxShare068.7z
p7zip -d VxShare069.7z
p7zip -d VxShare070.7z
p7zip -d VxShare071.7z
p7zip -d VxShare072.7z
p7zip -d VxShare073.7z
p7zip -d VxShare074.7z
p7zip -d VxShare075.7z
p7zip -d VxShare076.7z
p7zip -d VxShare077.7z
p7zip -d VxShare078.7z
p7zip -d VxShare079.7z
p7zip -d VxShare080.7z
p7zip -d VxShare081.7z
p7zip -d VxShare082.7z
p7zip -d VxShare083.7z
p7zip -d VxShare084.7z
p7zip -d VxShare085.7z
p7zip -d VxShare086.7z
p7zip -d VxShare087.7z
p7zip -d VxShare088.7z
p7zip -d VxShare089.7z
p7zip -d VxShare090.7z
p7zip -d VxShare091.7z
p7zip -d VxShare092.7z
p7zip -d VxShare093.7z
p7zip -d VxShare094.7z
p7zip -d VxShare095.7z
p7zip -d VxShare096.7z
p7zip -d VxShare097.7z
p7zip -d VxShare098.7z
p7zip -d VxShare099.7z
p7zip -d VxShare100.7z
p7zip -d VxShare101.7z
p7zip -d VxShare102.7z
p7zip -d VxShare103.7z
p7zip -d VxShare104.7z
p7zip -d VxShare105.7z
p7zip -d VxShare106.7z
p7zip -d VxShare107.7z
p7zip -d VxShare108.7z
p7zip -d VxShare109.7z
p7zip -d VxShare110.7z
p7zip -d VxShare111.7z
p7zip -d VxShare112.7z
p7zip -d VxShare113.7z
p7zip -d VxShare114.7z
p7zip -d VxShare115.7z
p7zip -d VxShare116.7z
p7zip -d VxShare117.7z
p7zip -d VxShare118.7z
p7zip -d VxShare119.7z
p7zip -d VxShare120.7z
p7zip -d VxShare121.7z
p7zip -d VxShare122.7z
p7zip -d VxShare123.7z
p7zip -d VxShare124.7z
p7zip -d VxShare125.7z
p7zip -d VxShare126.7z
p7zip -d VxShare127.7z
p7zip -d VxShare128.7z
p7zip -d VxShare129.7z
p7zip -d VxShare130.7z
p7zip -d VxShare131.7z
p7zip -d VxShare132.7z
p7zip -d VxShare133.7z
p7zip -d VxShare134.7z
p7zip -d VxShare135.7z
p7zip -d VxShare136.7z
p7zip -d VxShare137.7z
p7zip -d VxShare138.7z
p7zip -d VxShare139.7z
p7zip -d VxShare140.7z
p7zip -d VxShare141.7z
p7zip -d VxShare142.7z
p7zip -d VxShare143.7z
p7zip -d VxShare144.7z
p7zip -d VxShare145.7z
p7zip -d VxShare146.7z
p7zip -d VxShare147.7z
p7zip -d VxShare148.7z
p7zip -d VxShare149.7z
p7zip -d VxShare150.7z

hashdb create FileBlock.Import
hashdb import FileBlock.Import VxShare000.DFXML
hashdb import FileBlock.Import VxShare001.DFXML
hashdb import FileBlock.Import VxShare002.DFXML
hashdb import FileBlock.Import VxShare003.DFXML
hashdb import FileBlock.Import VxShare004.DFXML
hashdb import FileBlock.Import VxShare005.DFXML
hashdb import FileBlock.Import VxShare006.DFXML
hashdb import FileBlock.Import VxShare007.DFXML
hashdb import FileBlock.Import VxShare008.DFXML
hashdb import FileBlock.Import VxShare009.DFXML
hashdb import FileBlock.Import VxShare010.DFXML
hashdb import FileBlock.Import VxShare011.DFXML
hashdb import FileBlock.Import VxShare012.DFXML
hashdb import FileBlock.Import VxShare013.DFXML
hashdb import FileBlock.Import VxShare014.DFXML
hashdb import FileBlock.Import VxShare015.DFXML
hashdb import FileBlock.Import VxShare016.DFXML
hashdb import FileBlock.Import VxShare017.DFXML
hashdb import FileBlock.Import VxShare018.DFXML
hashdb import FileBlock.Import VxShare019.DFXML
hashdb import FileBlock.Import VxShare020.DFXML
hashdb import FileBlock.Import VxShare021.DFXML
hashdb import FileBlock.Import VxShare022.DFXML
hashdb import FileBlock.Import VxShare023.DFXML
hashdb import FileBlock.Import VxShare024.DFXML
hashdb import FileBlock.Import VxShare025.DFXML
hashdb import FileBlock.Import VxShare026.DFXML
hashdb import FileBlock.Import VxShare027.DFXML
hashdb import FileBlock.Import VxShare028.DFXML
hashdb import FileBlock.Import VxShare029.DFXML
hashdb import FileBlock.Import VxShare030.DFXML
hashdb import FileBlock.Import VxShare031.DFXML
hashdb import FileBlock.Import VxShare032.DFXML
hashdb import FileBlock.Import VxShare033.DFXML
hashdb import FileBlock.Import VxShare034.DFXML
hashdb import FileBlock.Import VxShare035.DFXML
hashdb import FileBlock.Import VxShare036.DFXML
hashdb import FileBlock.Import VxShare037.DFXML
hashdb import FileBlock.Import VxShare038.DFXML
hashdb import FileBlock.Import VxShare039.DFXML
hashdb import FileBlock.Import VxShare040.DFXML
hashdb import FileBlock.Import VxShare041.DFXML
hashdb import FileBlock.Import VxShare042.DFXML
hashdb import FileBlock.Import VxShare043.DFXML
hashdb import FileBlock.Import VxShare044.DFXML
hashdb import FileBlock.Import VxShare045.DFXML
hashdb import FileBlock.Import VxShare046.DFXML
hashdb import FileBlock.Import VxShare047.DFXML
hashdb import FileBlock.Import VxShare048.DFXML
hashdb import FileBlock.Import VxShare049.DFXML
hashdb import FileBlock.Import VxShare050.DFXML
hashdb import FileBlock.Import VxShare051.DFXML
hashdb import FileBlock.Import VxShare052.DFXML
hashdb import FileBlock.Import VxShare053.DFXML
hashdb import FileBlock.Import VxShare054.DFXML
hashdb import FileBlock.Import VxShare055.DFXML
hashdb import FileBlock.Import VxShare056.DFXML
hashdb import FileBlock.Import VxShare057.DFXML
hashdb import FileBlock.Import VxShare058.DFXML
hashdb import FileBlock.Import VxShare059.DFXML
hashdb import FileBlock.Import VxShare060.DFXML
hashdb import FileBlock.Import VxShare061.DFXML
hashdb import FileBlock.Import VxShare062.DFXML
hashdb import FileBlock.Import VxShare063.DFXML
hashdb import FileBlock.Import VxShare064.DFXML
hashdb import FileBlock.Import VxShare065.DFXML
hashdb import FileBlock.Import VxShare066.DFXML
hashdb import FileBlock.Import VxShare067.DFXML
hashdb import FileBlock.Import VxShare068.DFXML
hashdb import FileBlock.Import VxShare069.DFXML
hashdb import FileBlock.Import VxShare070.DFXML
hashdb import FileBlock.Import VxShare071.DFXML
hashdb import FileBlock.Import VxShare072.DFXML
hashdb import FileBlock.Import VxShare073.DFXML
hashdb import FileBlock.Import VxShare074.DFXML
hashdb import FileBlock.Import VxShare075.DFXML
hashdb import FileBlock.Import VxShare076.DFXML
hashdb import FileBlock.Import VxShare077.DFXML
hashdb import FileBlock.Import VxShare078.DFXML
hashdb import FileBlock.Import VxShare079.DFXML
hashdb import FileBlock.Import VxShare080.DFXML
hashdb import FileBlock.Import VxShare081.DFXML
hashdb import FileBlock.Import VxShare082.DFXML
hashdb import FileBlock.Import VxShare083.DFXML
hashdb import FileBlock.Import VxShare084.DFXML
hashdb import FileBlock.Import VxShare085.DFXML
hashdb import FileBlock.Import VxShare086.DFXML
hashdb import FileBlock.Import VxShare087.DFXML
hashdb import FileBlock.Import VxShare088.DFXML
hashdb import FileBlock.Import VxShare089.DFXML
hashdb import FileBlock.Import VxShare090.DFXML
hashdb import FileBlock.Import VxShare091.DFXML
hashdb import FileBlock.Import VxShare092.DFXML
hashdb import FileBlock.Import VxShare093.DFXML
hashdb import FileBlock.Import VxShare094.DFXML
hashdb import FileBlock.Import VxShare095.DFXML
hashdb import FileBlock.Import VxShare096.DFXML
hashdb import FileBlock.Import VxShare097.DFXML
hashdb import FileBlock.Import VxShare098.DFXML
hashdb import FileBlock.Import VxShare099.DFXML
hashdb import FileBlock.Import VxShare100.DFXML
hashdb import FileBlock.Import VxShare101.DFXML
hashdb import FileBlock.Import VxShare102.DFXML
hashdb import FileBlock.Import VxShare103.DFXML
hashdb import FileBlock.Import VxShare104.DFXML
hashdb import FileBlock.Import VxShare105.DFXML
hashdb import FileBlock.Import VxShare106.DFXML
hashdb import FileBlock.Import VxShare107.DFXML
hashdb import FileBlock.Import VxShare108.DFXML
hashdb import FileBlock.Import VxShare109.DFXML
hashdb import FileBlock.Import VxShare110.DFXML
hashdb import FileBlock.Import VxShare111.DFXML
hashdb import FileBlock.Import VxShare112.DFXML
hashdb import FileBlock.Import VxShare113.DFXML
hashdb import FileBlock.Import VxShare114.DFXML
hashdb import FileBlock.Import VxShare115.DFXML
hashdb import FileBlock.Import VxShare116.DFXML
hashdb import FileBlock.Import VxShare117.DFXML
hashdb import FileBlock.Import VxShare118.DFXML
hashdb import FileBlock.Import VxShare119.DFXML
hashdb import FileBlock.Import VxShare120.DFXML
hashdb import FileBlock.Import VxShare121.DFXML
hashdb import FileBlock.Import VxShare122.DFXML
hashdb import FileBlock.Import VxShare123.DFXML
hashdb import FileBlock.Import VxShare124.DFXML
hashdb import FileBlock.Import VxShare125.DFXML
hashdb import FileBlock.Import VxShare126.DFXML
hashdb import FileBlock.Import VxShare127.DFXML
hashdb import FileBlock.Import VxShare128.DFXML
hashdb import FileBlock.Import VxShare129.DFXML
hashdb import FileBlock.Import VxShare130.DFXML
hashdb import FileBlock.Import VxShare131.DFXML
hashdb import FileBlock.Import VxShare132.DFXML
hashdb import FileBlock.Import VxShare133.DFXML
hashdb import FileBlock.Import VxShare134.DFXML
hashdb import FileBlock.Import VxShare135.DFXML
hashdb import FileBlock.Import VxShare136.DFXML
hashdb import FileBlock.Import VxShare137.DFXML
hashdb import FileBlock.Import VxShare138.DFXML
hashdb import FileBlock.Import VxShare139.DFXML
hashdb import FileBlock.Import VxShare140.DFXML
hashdb import FileBlock.Import VxShare141.DFXML
hashdb import FileBlock.Import VxShare142.DFXML
hashdb import FileBlock.Import VxShare143.DFXML
hashdb import FileBlock.Import VxShare144.DFXML
hashdb import FileBlock.Import VxShare145.DFXML
hashdb import FileBlock.Import VxShare146.DFXML
hashdb import FileBlock.Import VxShare147.DFXML
hashdb import FileBlock.Import VxShare148-DFXML.DFXML
hashdb import FileBlock.Import VxShare149-DFXML.DFXML
hashdb import FileBlock.Import VxShare150.DFXML
hashdb size FileBlock.Import

hashdb create FileBlock.Info
hashdb subtract FileBlock.Import FileBlock.White FileBlock.Info
hashdb size FileBlock.Info
