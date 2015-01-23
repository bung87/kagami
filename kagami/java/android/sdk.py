import os
import socket

host = 'dl-ssl.google.com'
mirror_host = 'mirrors.neusoft.edu.cn'

hosts_path_map = {
    'nt':r'C:\Windows\System32\drivers\etc\hosts',
    'posix':'/etc/hosts',
    'mac':'/Private/etc/hosts'
}

try:
    with open(hosts_path_map[os.name],'a') as f:
        try:
            host_ip = socket.gethostbyname(mirror_host)
        except socket.gaierror as e:
            raise e
        f.writelines('%s %s' % (host_ip, host)+os.linesep)
except Exception as e:
    raise e