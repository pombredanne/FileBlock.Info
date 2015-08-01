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
Follow @FileBlocks on Twitter for more information or send a Direct Message a.k.a. DM for more details.
<br><br>
UPDATE: Started V2 with all the great artifacts but way less bandwidth requirements for distribution.
##Code
https://github.com/jblukach/hashdb-api
