#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  openbox-pipemenu-recent.py
#  
#  Copyright 2017 kirbylife <https://github.com/ImNotRoot>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import xml.etree.ElementTree
import os

XMLFILE=os.environ['HOME']+"/.local/share/recently-used.xbel"

def setItem(name,file=""):
	if file not in "":
		print "<item label='"+name+"'><action name='Execute'><command>xdg-open "+file+"</command></action></item>"
	else:
		print "<item label='"+name+"'></item>"

def main(args):
	
	### Header ###
	print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
	print "<openbox_pipe_menu>"
	###        ###
	
	e = xml.etree.ElementTree.parse(XMLFILE).getroot()
	files=e.findall("bookmark")
	for c in range(len(files)-1,len(files)-11,-1):
		file=files[c].get("href")
		if "file://" in file:
			setItem(file[file.rfind("/")+1:],file[7:])
	
	### Footer ###
	print "</openbox_pipe_menu>"
	###        ###
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
