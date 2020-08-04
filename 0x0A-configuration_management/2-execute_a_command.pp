# Kill process with puppet
exec { 'kill_process':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  returns => '0',
}
