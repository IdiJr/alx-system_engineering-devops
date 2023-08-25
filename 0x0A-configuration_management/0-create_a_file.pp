# creates a file in /tmp.
file { '/tmp/school':
  ensure  => present,
  mode    => '0074',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
