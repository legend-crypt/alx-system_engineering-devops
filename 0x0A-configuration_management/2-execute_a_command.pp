# kill a runing process
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin/', '/usr/sbin']
}
