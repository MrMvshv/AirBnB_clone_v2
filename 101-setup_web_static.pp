# sets up server environment

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/data/web_static/releases/test/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/shared/':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure => file,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0644',
    content => '<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test/',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  exec { 'chown':
    command     => '/bin/chown -R ubuntu:ubuntu /data/',
    refreshonly => true,
  }

  file_line { 'nginx_config':
      path   => '/etc/nginx/sites-available/default',
      line   => "location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n",
      match  => "^\\s*location / {",
      before => "location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n",
      require=> Package['nginx'],
      notify=> Service['nginx'],
      replace=> true,
      }
}

include nginx
