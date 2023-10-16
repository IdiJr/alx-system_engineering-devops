# a puppet manifest that fixes failed requests to server

exec {'sed':
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 15000\"/" /etc/default/nginx',
  provider => 'shell',
}

exec {'restart':
  command  => 'service nginx restart',
  provider => 'shell',
}
