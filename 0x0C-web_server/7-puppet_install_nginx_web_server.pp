# This manifest configures ubuntu server using nginx
exec {'update':
  command => '/bin/apt-get update',
}
package {'nginx':
  ensure   => 'installed',
  provider => apt,
  name     => 'nginx',
  require  => Exec['update'],
}

file {'web-content':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  require => Package['nginx'],
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

$config_content = "server {
	listen 80;
	server_name geekpace.tech;
	root /var/www/html;
	index index.html index.htm;
	location /redirect_me {
		return 301 https://www.youtube.com;
	}
}"

file {'config':
  path    => '/etc/nginx/sites-available/default',
  content => $config_content,
  require => File['web-content'],
  notify  => Service['nginx'],
}

service { 'nginx':
    ensure => true,
    enable => true,
    name   => 'nginx',
}
