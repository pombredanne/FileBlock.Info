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
Follow @FileBlocks on Twitter to Direct Message a.k.a. DM a request for a download link.  The collection is about 105 GB containing twenty four split compressed 7zip files that when unpacked will require 265 GB of disk space. HashDB-API Project: https://github.com/jblukach/hashdb-api too.
<table>
<thead>
<th>File</th>
<th>MD5</th>
</thead>
<tr><td>FileBlock.Info.7z.001</td><td>c1046d11156386a161f2a855529a04c0</td></tr>
<tr><td>FileBlock.Info.7z.002</td><td>19175d7ba4f7e1164101657428f7201a</td></tr>
<tr><td>FileBlock.Info.7z.003</td><td>e478750849d4ad4a6a63fe6ce3df4ce6</td></tr>
<tr><td>FileBlock.Info.7z.004</td><td>07e50d460dad894e880809719e44748c</td></tr>
<tr><td>FileBlock.Info.7z.005</td><td>a5e5a91ff18c0c76f1aac4f2030b0cc7</td></tr>
<tr><td>FileBlock.Info.7z.006</td><td>ee11675760ccad1cc36b882c888fc74d</td></tr>
<tr><td>FileBlock.Info.7z.007</td><td>f95a603fbf5320220df0ecfb6d3c5bd2</td></tr>
<tr><td>FileBlock.Info.7z.008</td><td>74d26bc4611142511381dc382c87aa4d</td></tr>
<tr><td>FileBlock.Info.7z.009</td><td>6528b5499bd90949bef3017b30491d3d</td></tr>
<tr><td>FileBlock.Info.7z.010</td><td>32488e54ea6a91928d6da4915eb07f2f</td></tr>
<tr><td>FileBlock.Info.7z.011</td><td>869ce9327c6d4241adae290c8735dc15</td></tr>
<tr><td>FileBlock.Info.7z.012</td><td>a00341a09a197100673a0e497146f200</td></tr>
<tr><td>FileBlock.Info.7z.013</td><td>852cbbb0f93321802c76009e3c78a817</td></tr>
<tr><td>FileBlock.Info.7z.014</td><td>b67a4c4b8b85916b092721245eecd534</td></tr>
<tr><td>FileBlock.Info.7z.015</td><td>7efed522ed93713f2502a122e66ac63b</td></tr>
<tr><td>FileBlock.Info.7z.016</td><td>44720a569cd1a8c4b339ef147853d043</td></tr>
<tr><td>FileBlock.Info.7z.017</td><td>a09c9c1c54a0cc5f0f98d2b5492b5c5b</td></tr>
<tr><td>FileBlock.Info.7z.018</td><td>d4717048ce81f9a16c312e8cd90c3bdc</td></tr>
<tr><td>FileBlock.Info.7z.019</td><td>56086f2656a812a0cbd5af3320bbb910</td></tr>
<tr><td>FileBlock.Info.7z.020</td><td>8f23fe37a40905b212b4295d7c6fe0b2</td></tr>
<tr><td>FileBlock.Info.7z.021</td><td>21e4afbdf7771180dc2ef43d7cf9022e</td></tr>
<tr><td>FileBlock.Info.7z.022</td><td>a7acfe1ee9e8914a7f9258e74d713d27</td></tr>
<tr><td>FileBlock.Info.7z.023</td><td>93378e39a3f6ca0f090798d4d3d54e32</td></tr>
<tr><td>FileBlock.Info.7z.024</td><td>bae391861c8353b235b76fbe29664c03</td></tr>
</table>
Run the following hashdb command to validate that the database has been reassembled and is functioning correctly after the transfer.
```
C:\>hashdb size FileBlock.Info
hash store size: 9542732353
source store size: 10369882
```
