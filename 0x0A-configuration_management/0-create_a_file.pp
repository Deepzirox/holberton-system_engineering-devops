# puppet create file
file { '/tmp/holberton':
      ensure  => present,
      content => 'I love Puppet',
      owner   => 'www-data',
      group   => 'www-data',
      mode    => '0744',
    }
