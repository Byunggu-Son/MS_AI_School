import imp

import socket

#hostname은 서버이름. pc에서는 pc이름. gethostbyname이름을 가지고 IPaddress를 뽑아주는 역할.
in_addr =  socket.gethostbyname(socket.gethostname())
print(in_addr) #실제 ip주소가 아님. ip주소는 2^8으로 4자리 되어있는게 ip주소.(2^8.2^8.2^8.2^8). ipaddress는 8*4 = 32bit 이건 IPv4, 6자리는 IPv6