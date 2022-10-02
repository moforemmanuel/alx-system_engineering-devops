#add custom header to nginx req/res headers, to identify which server is selected by the HAProxy

exec {'cHeader':
	provider => shell,
	path => '/usr/bin:/usr/sbin:/bin',
	command => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo sed -i '/^\tserver_name/a \\n\tadd_header X-Served-By $HOSTNAME;\n' /etc/nginx/sites-available/default ; sudo service nginx restart',
}

#exec {'header':
#  provider    => shell,
#  command     => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; header_str="location \/ {\n\t\tadd_header X-Served-By \$hostname;" ; sudo sed -i "s/location \/ {/$header_str/" /etc/nginx/sites-available/default ; sudo service nginx restart',
#}

