# Python format map/database configuration. 
# Move this file to 'conf/settings.py', and add some 'favicon' information in the favicon folder e.g. realfavicongenerator.com
# You must also set your project name manually in your 'favicon/manifest.json' file.

# Any line starting with # will be ignored.

project_name = 		'example'
project_description = 	'Example map'

# files & folders & urls - set these by hand.

webserver_url = 	''
www_folder = 		'/var/www/html'
wms_folder = 		'/var/www/wms'

# files & folders & urls - these are automatically calculated.

www_url = 		webserver_url+'/'+project_name
wms_url = 		webserver_url+'/wms/'+project_name	
www_project_folder = 	www_folder+'/'+project_name
wms_project_folder = 	wms_folder+'/'+project_name
getfeature_template = 	wms_project_folder+'/query_template.html'
information_template = 	wms_project_folder+'/query_template_info.html'
wms_log_folder     =    wms_project_folder+'/log'
error_log = 		wms_log_folder+'/error_log.log'
mapfile = 		wms_project_folder+'/'+project_name+'.map'
wwwfile = 		www_project_folder+'/index.html'

# DB settings - set these by hand. 

database_server = 	''
database_port = 	'5432'
database_name = 	''

database_username = 	''      #Don't store this file in a public git repo!
database_password = 	''      #Make this file a separate git repo.
database_schema = 	''

database_table_prefix = 'map_'		#e.g. ess_map_0, ess_map_1_1_1, overview_1_3, overview_wms ... 

# Map settings - set these by hand. This page may be useful for extents: (https://epsg.io/3857/map)

map_srid = 		'3857'		# web mercator - compatible with google/bing tile maps
map_extent_min_x = 	'500000'        # these are extents for norway
map_extent_max_x = 	'2000000'
map_extent_min_y = 	'7900000'
map_extent_max_y = 	'11500000'

map_min_scale = 	'300'		# This is for zoom scale.
map_max_scale = 	'1000000' 	# This is for zoom scale.
map_max_size_pixels = 	'5000'          # This is the pixel size limit for mapserver images.

map_ol_center = '[1202896.139476, 8324578.895374]'
map_ol_zoom = '14'

# Map layers - set these by hand. 
# Notice that the last line of this doesn't have a comma at the end!

map_layers = [
'main_wms', 	'Example overview layer', 
'2_wms',	'Example layer 2'
] 
