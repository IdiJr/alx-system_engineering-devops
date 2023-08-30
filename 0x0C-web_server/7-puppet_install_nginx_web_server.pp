# Configures an Nginx server using Puppet instead of Bash.

package { 'nginx':
    ensure => installed,
}

file {'/var/www/html/index.html':
    content => 'Hello World!',
}

file_line { 'redirection configuration':
    path  =>  '/etc/nginx/sites-enabled/default',
    after =>  'server_name _;',
    line  =>  'rewrite ^/redirect_me https://youtu.be/nuNvRFOXn3w?si=JvnxyjMZY0E4ifC4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package[ 'nginx' ],
}
