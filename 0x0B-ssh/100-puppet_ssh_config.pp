# wed like you to set up your client SSH configuration file so that you can connect to a server without typing a password
file_line { 'chance key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => 'IdentityFile ~/.ssh/id_rsa',
}
file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}