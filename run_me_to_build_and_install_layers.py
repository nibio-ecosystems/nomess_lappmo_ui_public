#!/usr/bin/python -B

# This program builds the mapserver and openlayers configuration files using templates
# and copies necessary files into the correct places, to achieve a working openlayers installation.

import os
import stat
import shutil
from string import Template

execfile('conf/settings.py')

# Global variable, used once in template.

def setup_mapserver_files():

	# open map template and substitute variables into the template
	with open('mapserver/mapserver_template.map','r') as input_template:
		input_string=input_template.read()
	mapfile_template = Template(input_string)
	substituted_string = mapfile_template.substitute(globals())

	# open layer template and substitute variables into the template for all layers
	with open('mapserver/mapserver_template_layer.map','r') as input_template:
		input_string=input_template.read()
	layer_template = Template(input_string)

	layers = zip(*[iter(map_layers)] * 2)   # group the name/description into pairs (name, description)
	layers_string=''			# initialise the target string for the layers text

	for layer in layers:
		layer_name = database_table_prefix+layer[0]   # join the prefix to the layer name
		layer_description = layer[1]	 	   
		layers_string += layer_template.substitute(dict(globals().items()+locals().items()))   # combine local/global definitions

	# generate the final mapfile from the completed pieces
	output_file = open(mapfile, 'w')   
	output_file.write(substituted_string)
	output_file.write(layers_string)
	output_file.write('END #map')
	print "Mapserver configuration file: done."

	# Copy mapserver HTTPD configuration file and WMS getfeature templates into place.
	shutil.copyfile('mapserver/mapserver_httpd.conf', '/etc/httpd/conf.d/mapserver.conf')
	shutil.copyfile('mapserver/query_template.html', getfeature_template)


def generate_openlayers_configuration():
	#shutil.copyfile('openlayers/', '/var/www/html/index.html')

	copy_all_files('openlayers/common',www_project_folder+'/common');
	copy_all_files('conf/favicon',www_project_folder+'/favicon');
	shutil.copyfile('conf/favicon/favicon.ico',www_project_folder+'/favicon.ico');

	# Generate layer code as variables to be substituted. (slightly different from mapserver approach above)

	project_maps_para=''
	project_maps_description_para=''

#	with open('openlayers/openlayers_template_layer.js','r') as input_template:
#		input_string=input_template.read()
#	layer_template = Template(input_string)

	layers = zip(*[iter(map_layers)] * 2)   # group the name/description into pairs (name, description)
	layers_string=''			# initialise the target string for the layers text

	for layer in layers:
                layer_name = database_table_prefix+layer[0]   # join the prefix to the layer
                layer_description = layer[1]

		project_maps_para +=  "'" + layer_name + "',\n"   	# CHECK: trailing ',' for blank map/ or accident? at end of project_maps_para
		project_maps_description_para += '      <option value="'+ layer_name + '">' + layer_description + '</option>\n'

	# open OL web template and substitute variables into the template
	with open('openlayers/openlayers_template.html','r') as input_template:
		input_string=input_template.read()
	wwwfile_template = Template(input_string)
	substituted_string = wwwfile_template.substitute(dict(globals().items()+locals().items()))

	# generate the final openlayer html file from the completed pieces
	output_file = open(wwwfile, 'w')   
	output_file.write(substituted_string)
	print "Openlayers configuration file: done."

 
       # create favicon folder (if it doesn't exist). for all files in favicon copy
       # create common folder, copy. edit html to reflect new location  of gps thing.
       



def reminder():
	print "Map files installed. Remember to restart apache: 'service httpd restart'"


def setup_folders(): 
	for i in [www_folder, wms_folder, www_project_folder, 
		  wms_project_folder, wms_log_folder, www_project_folder+'/favicon',
		  www_project_folder+'/common']:
		check_folder(i)
	os.chmod(wms_log_folder, 0777)


def check_folder(directory):
	if not os.path.exists(directory):
		print 'Folder '+directory+' does not exist - creating it now.'
		os.makedirs(directory)


def copy_all_files(srcdir, dstdir):
	for file in os.listdir(srcdir):
		print file  # testing
		src_file = os.path.join(srcdir, file)
		dst_file = os.path.join(dstdir, file)
		shutil.copyfile(src_file, dst_file)

# Main program here

def main():
	setup_folders()
	setup_mapserver_files()
	generate_openlayers_configuration()
	reminder()

if __name__ == "__main__":
	main()





