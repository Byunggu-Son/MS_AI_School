import imp

import socket

#hostname은 서버이름. pc에서는 pc이름. gethostbyname이름을 가지고 IPaddress를 뽑아주는 역할.
in_addr =  socket.gethostbyname(socket.gethostname())
print(in_addr) #실제 ip주소가 아님. 