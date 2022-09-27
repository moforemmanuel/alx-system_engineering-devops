# create ssh config file
exec { 'create_ssh_config':
	command => 'echo -e "Host *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no" > ~/.ssh/config'
	path => ['/usr/bin', '/usr/sbin', '/bin']
}
