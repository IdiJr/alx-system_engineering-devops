# creates a file in /tmp.

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0074',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
