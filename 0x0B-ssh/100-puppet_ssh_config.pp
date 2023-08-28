#set up your client SSH configuration file so that you can connect to a server without typing a password.
exec {'ssh':
  command => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin',
  }
