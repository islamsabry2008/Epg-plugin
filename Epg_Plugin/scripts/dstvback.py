#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from time import sleep
import os,io,re


with io.open('/usr/lib/enigma2/python/Plugins/Extensions/Epg_Plugin/times/dstvback.txt','r') as f:
    time_zone = f.read().strip()
    
path = '/etc/epgimport/dstv.xml'

print "Downloading SuperSport epg guide\nPlease wait...."  

os.system('wget -q "--no-check-certificate" http://github.com/ziko-ZR1/XML/blob/master/dstv.xml?raw=true -O '+path+'')

sleep(1)

f = open(path,'r')
time_of = re.search(r'[+#-]+\d{4}',f.read())
f.close()

print "changing to your timezone please wait...."

if os.path.exists(path):
    if time_of !=None:
        with io.open(path,encoding="utf-8") as f:
            newText=f.read().decode('utf-8').replace(time_of.group(), time_zone)
            with io.open(path, "w",encoding="utf-8") as f:
                f.write((newText).decode('utf-8'))
    else:
        print "file is empty"
        
print "dstv.xml donwloaded with succes"


if not os.path.exists('/etc/epgimport/custom.channels.xml'):
    print('Downloading custom.channels config')
    os.system('wget -q "--no-check-certificate" https://github.com/ziko-ZR1/Epg-plugin/blob/master/Epg_Plugin/configs/custom.channels.xml?raw=true -O /etc/epgimport/custom.channels.xml')
        
if not os.path.exists('/etc/epgimport/custom.sources.xml'):
    print('Downloading custom sources config')
    os.system('wget -q "--no-check-certificate" https://github.com/ziko-ZR1/Epg-plugin/blob/master/Epg_Plugin/configs/custom.sources.xml?raw=true -O /etc/epgimport/custom.sources.xml')


if not os.path.exists('/etc/epgimport/elcinema.channels.xml'):
    print('Downloading elcinema channels config')
    os.system('wget -q "--no-check-certificate" https://github.com/ziko-ZR1/Epg-plugin/blob/master/Epg_Plugin/configs/elcinema.channels.xml?raw=true -O /etc/epgimport/elcinema.channels.xml')


if not os.path.exists('/etc/epgimport/dstv.channels.xml'):
    print('Downloading dstv channels config')
    os.system('wget -q "--no-check-certificate" https://github.com/ziko-ZR1/Epg-plugin/blob/master/Epg_Plugin/configs/dstv.channels.xml?raw=true -O /etc/epgimport/dstv.channels.xml')