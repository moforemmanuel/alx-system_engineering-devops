#add custom header to nginx req/res headers, to identify which server is selected by the HAProxy

exec {'set_haproxy_header':
	provider => shell,
	path => '/usr/bin:/usr/sbin:/bin',
	command => 'sudo apt-get update ; sudo apt-get -y install nginx ; sudo sed -i '/^\tserver_name/a \\n\tadd_header X-Served-By $HOSTNAME;\n' /etc/nginx/sites-available/default ; sudo service nginx restart',
}

