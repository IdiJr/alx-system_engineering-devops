# Configures an Nginx server using Puppet instead of Bash.

package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.html':
    content => 'Hello World!',
}

file_line {'configure redirection':
    path  =>  '/etc/nginx/sites-available/default',
    after =>  'server_name _;',
    line  =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://youtu.be/nuNvRFOXn3w?si=JvnxyjMZY0E4ifC4 permanent;\n\t}\n",
}

service {'nginx':
    ensure => running,
}
