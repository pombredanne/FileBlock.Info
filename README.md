# FileBlock.Info
##Build HashDB
Run the following bulk_extractor command to generate a sector hashdb of the extracted VirusShare.com torrent files.  The database will be found in the bulk_extractor output folder that by default is called hashdb.hdb that I typically rename to VxShare159 for example.
```
bulk_extractor -x accts -x aes -x base64 -x elf -x email -x exif -x find -x gps -x gzip -x hiberfile -x httplogs -x json -x kml -x msxml -x net -x pdf -x rar -x sqlite -x vcard -x windirs -x winlnk -x winpe -x winprefetch -x zip -e hashdb -o VxShare159_Out -S hashdb_mode=import -S hashdb_import_repository_name=VxShare159 -S hashdb_block_size=512 -S hashdb_import_sector_size=512 -R VirusShare_00159
```
Consolidate the sector databases into one collection using the following hashdb commands.  Only create the sector database the first time that blocks are added.
```
hashdb create -p 512 FileBlock.Import
hashdb add VxShare159 FileBlock.Import
...
```
Download the NIST NSRL blocks from http://www.nsrl.nist.gov/ftp/MD5B512/ and consolidate into a single collection using these hashdb commands for each set.
```
hashdb create -p 512 FileBlock.NSRL
hashdb import_tab FileBlock.NSRL MD5B512_0.tab
...
```
Finally subtract the whitelist block hashes from the blacklist block hashes to help limit false postives from code reuse.
```
hashdb create -p 512 FileBlock.Info
hashdb subtract FileBlock.Import FileBlock.NSRL FileBlock.Info
```
##Use HashDB
Scan files, images and memory using this bulk_extractor command to locate matching sector block hashes using the FileBlock.Info hashdb database.
```
bulk_extractor -e hashdb -S hashdb_mode=scan -S hashdb_scan_path_or_socket=FileBlock.Info -S hashdb_block_size=512 -o be2_out be2.vmem 
```
Review the identified_blocks.txt file for matches or use the hashdb command expand_identified_blocks for more details on associated samples.
```
hashdb expand_identified_blocks FileBlock.Info identified_blocks.txt
```
##Aquire Copy
Follow @FileBlocks on Twitter for more information or send a Direct Message a.k.a. DM for specific questions.
<br><br>
http://download.fileblock.info/VxShare000.7z<br>
http://download.fileblock.info/VxShare001.7z<br>
http://download.fileblock.info/VxShare002.7z<br>
http://download.fileblock.info/VxShare003.7z<br>
http://download.fileblock.info/VxShare004.7z<br>
http://download.fileblock.info/VxShare005.7z<br>
http://download.fileblock.info/VxShare006.7z<br>
http://download.fileblock.info/VxShare007.7z<br>
http://download.fileblock.info/VxShare008.7z<br>
http://download.fileblock.info/VxShare009.7z<br>
http://download.fileblock.info/VxShare010.7z<br>
http://download.fileblock.info/VxShare011.7z<br>
http://download.fileblock.info/VxShare012.7z<br>
http://download.fileblock.info/VxShare013.7z<br>
http://download.fileblock.info/VxShare014.7z<br>
http://download.fileblock.info/VxShare015.7z<br>
http://download.fileblock.info/VxShare016.7z<br>
http://download.fileblock.info/VxShare017.7z<br>
http://download.fileblock.info/VxShare018.7z<br>
http://download.fileblock.info/VxShare019.7z<br>
http://download.fileblock.info/VxShare020.7z<br>
http://download.fileblock.info/VxShare021.7z<br>
http://download.fileblock.info/VxShare022.7z<br>
http://download.fileblock.info/VxShare023.7z<br>
http://download.fileblock.info/VxShare024.7z<br>
http://download.fileblock.info/VxShare025.7z<br>
http://download.fileblock.info/VxShare026.7z<br>
http://download.fileblock.info/VxShare027.7z<br>
http://download.fileblock.info/VxShare028.7z<br>
http://download.fileblock.info/VxShare029.7z<br>
http://download.fileblock.info/VxShare030.7z<br>
http://download.fileblock.info/VxShare031.7z<br>
http://download.fileblock.info/VxShare032.7z<br>
http://download.fileblock.info/VxShare033.7z<br>
http://download.fileblock.info/VxShare034.7z<br>
http://download.fileblock.info/VxShare035.7z<br>
http://download.fileblock.info/VxShare036.7z<br>
http://download.fileblock.info/VxShare037.7z<br>
http://download.fileblock.info/VxShare038.7z<br>
http://download.fileblock.info/VxShare039.7z<br>
http://download.fileblock.info/VxShare040.7z<br>
http://download.fileblock.info/VxShare041.7z<br>
http://download.fileblock.info/VxShare042.7z<br>
http://download.fileblock.info/VxShare043.7z<br>
http://download.fileblock.info/VxShare044.7z<br>
http://download.fileblock.info/VxShare045.7z<br>
http://download.fileblock.info/VxShare046.7z<br>
http://download.fileblock.info/VxShare047.7z<br>
http://download.fileblock.info/VxShare048.7z<br>
http://download.fileblock.info/VxShare049.7z<br>
http://download.fileblock.info/VxShare050.7z<br>
http://download.fileblock.info/VxShare051.7z<br>
http://download.fileblock.info/VxShare052.7z<br>
http://download.fileblock.info/VxShare053.7z<br>
http://download.fileblock.info/VxShare054.7z<br>
http://download.fileblock.info/VxShare055.7z<br>
http://download.fileblock.info/VxShare056.7z<br>
http://download.fileblock.info/VxShare057.7z<br>
http://download.fileblock.info/VxShare058.7z<br>
http://download.fileblock.info/VxShare059.7z<br>
http://download.fileblock.info/VxShare060.7z<br>
http://download.fileblock.info/VxShare061.7z<br>
http://download.fileblock.info/VxShare062.7z<br>
http://download.fileblock.info/VxShare063.7z<br>
http://download.fileblock.info/VxShare064.7z<br>
http://download.fileblock.info/VxShare065.7z<br>
http://download.fileblock.info/VxShare066.7z<br>
http://download.fileblock.info/VxShare067.7z<br>
http://download.fileblock.info/VxShare068.7z<br>
http://download.fileblock.info/VxShare069.7z<br>
http://download.fileblock.info/VxShare070.7z<br>
http://download.fileblock.info/VxShare071.7z<br>
http://download.fileblock.info/VxShare072.7z<br>
http://download.fileblock.info/VxShare073.7z<br>
http://download.fileblock.info/VxShare074.7z<br>
http://download.fileblock.info/VxShare075.7z<br>
http://download.fileblock.info/VxShare076.7z<br>
http://download.fileblock.info/VxShare077.7z<br>
http://download.fileblock.info/VxShare078.7z<br>
http://download.fileblock.info/VxShare079.7z<br>
http://download.fileblock.info/VxShare080.7z<br>
http://download.fileblock.info/VxShare081.7z<br>

##Code
https://github.com/jblukach/hashdb-api
