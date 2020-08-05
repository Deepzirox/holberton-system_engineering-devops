 # Configure ssh config
 
file_line {'Declare identity file':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton'
}
 
file_line {'Turn off passwd auth':
  replace => true,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no'
}
