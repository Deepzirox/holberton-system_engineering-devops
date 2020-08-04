# puppet create file
$content = 'I Love Puppet'

file { '/tmp/holberton':
      ensure  => present,
      content => $content,
      owner   => www-data,
      group   => www-data,
      mode    => '0744',
    }
