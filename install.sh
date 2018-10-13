#!/bin/bash

# setup mapserver + deps

yum -y install mapserver httpd

cp /usr/libexec/mapserver /var/www/cgi-bin/mapserv

# setup mapserver wms and font folders

mkdir -p /var/www/wms
mkdir -p /var/www/wms/fonts
touch /var/www/wms/fonts/fonts.list   # add fonts here if you are using map legends etc.

# any permissions to set?

# Openlayers - no server dependencies.


