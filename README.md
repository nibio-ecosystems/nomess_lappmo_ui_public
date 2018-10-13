NO-MESS Ecosystems LAPPMO web stack.  (Linux, Apache, Postgres, Postgis, Mapserver, Openlayers 3)
This project folder configures everything needed for web based visualisation and apps.

*Warning! Mapserver is only automatically installed by yum for Centos 6. Centos 7 requires a manual install.*

To configure the project settings and layers, look at:

	./conf/settings.py

To change the site's favicon / app-icon, replace this folder with another from realfavicongenerator.

	./conf/favicon

To install necessary applications on a new web/wms server, run this as root:

	./install.sh 

To build & install the configurations for mapserver & openlayers, run this as root:

	./run_me_to_build_and_install_layers.py