exec {'set_haproxy_header':
	provider => shell,
	command => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo sed -i '/^\tserver_name/a \\n\tadd_header X-Served-By $HOSTNAME;\n' /etc/nginx/sites-available/default ; sudo service nginx restart',
}

