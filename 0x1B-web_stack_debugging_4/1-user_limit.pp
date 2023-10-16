# puppet manifest that changes the OS configuration so that it is possible
# to login with the holberton user and open a file without any error message.

exec {'hard nofile change':
  command  => 'sed -i "s/nofile 5/nofile 6000/" /etc/security/limits.conf',
  provider => 'shell',
  before   => Exec['soft nofile change'],
}
exec {'soft nofile change':
  command  => 'sed -i "s/nofile 4/nofile 5000/" /etc/security/limits.conf',
  provider => 'shell',
}
